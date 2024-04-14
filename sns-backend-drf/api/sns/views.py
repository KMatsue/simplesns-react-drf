from rest_framework import authentication, permissions
from django.db.models import Q
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from rest_framework import status
from rest_framework.response import Response
from api.sns import serializers
from api.sns.models import FriendRequest, Message
# Create your views here.


class FriendRequestViewSet(viewsets.ModelViewSet):
    queryset = FriendRequest.objects.all()
    serializer_class = serializers.FriendRequestSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return self.queryset.filter(Q(askTo=self.request.user) | Q(askFrom=self.request.user))

    def perform_create(self, serializer):
        try:
            serializer.save(askFrom=self.request.user)
        except ValueError:
            raise ValidationError("ユーザーは一意のリクエストしか持つことができません")

    def destroy(self, request, *args, **kwargs):
        """Deleteメソッドを許可しないようにする"""

        response = {'message': 'Delete is not allowed !'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, *args, **kwargs):
        """PATCHメソッドを許可しないようにする"""

        response = {'message': 'Patch is not allowed !'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)


class MessageViewSet(viewsets.ModelViewSet):

    queryset = Message.objects.all()
    serializer_class = serializers.MessageSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return self.queryset.filter(sender=self.request.user)

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)

    def destroy(self, request, *args, **kwargs):
        response = {'message': 'Delete DM is not allowed'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        response = {'message': 'Update DM is not allowed'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, *args, **kwargs):
        response = {'message': 'Patch DM is not allowed'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)


class InboxListView(viewsets.ReadOnlyModelViewSet):

    queryset = Message.objects.all()
    serializer_class = serializers.MessageSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return self.queryset.filter(receiver=self.request.user)
