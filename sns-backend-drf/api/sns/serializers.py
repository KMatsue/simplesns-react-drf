from rest_framework import serializers
from api.accounts.models import User, Profile
from api.sns.models import FriendRequest, Message
from django.db.models import Q


class FriendRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendRequest
        fields = ('id', 'askFrom', 'askTo', 'approved')
        extra_kwargs = {'askFrom': {'read_only': True}}


class FriendsFilter(serializers.PrimaryKeyRelatedField):
    '''メッセージをフレンドのみに送るためのフィルター'''

    def get_queryset(self):
        request = self.context['request']
        friends = FriendRequest.objects.filter(Q(askTo=request.user) & Q(approved=True))

        list_friend = []
        for friend in friends:
            list_friend.append(friend.askFrom.id)

        queryset = User.objects.filter(id__in=list_friend)
        return queryset


class MessageSerializer(serializers.ModelSerializer):

    receiver = FriendsFilter()

    class Meta:
        model = Message
        fields = ('id', 'message', 'receiver')
        extra_kwargs = {'sender': {'read_only': True}}
