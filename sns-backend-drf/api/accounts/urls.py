from django.urls import path, include
from api.accounts import views

from rest_framework.routers import DefaultRouter

app_name = 'accounts'

router = DefaultRouter()
router.register('profile', views.ProfileViewSet)


urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('myprofile/', views.MyProfileListView.as_view(), name='myprofile'),
    path('', include(router.urls))
]
