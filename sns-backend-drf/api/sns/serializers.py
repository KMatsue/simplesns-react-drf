from rest_framework import serializers
from api.sns.models import FriendRequest, Message


class FriendRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendRequest
        fields = ('id', 'askFrom', 'askTo', 'approved')
        extra_kwargs = {'askFrom': {'read_only': True}}


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'message', 'receiver')
        extra_kwargs = {'sender': {'read_only': True}}
