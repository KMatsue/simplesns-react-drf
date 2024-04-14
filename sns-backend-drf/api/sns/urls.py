from django.urls import path, include

from rest_framework.routers import DefaultRouter
from api.sns import views


app_name = 'sns'

router = DefaultRouter()
router.register('approval', views.FriendRequestViewSet)
router.register('message', views.MessageViewSet, basename="message")
router.register('inbox', views.InboxListView, basename='inbox')

urlpatterns = [
    path('', include(router.urls))
]
