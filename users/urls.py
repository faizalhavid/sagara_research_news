from django.urls import path
from .views import UserAPIView
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('users/', UserAPIView.as_view(), name='user-post'),
]