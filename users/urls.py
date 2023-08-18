from django.urls import path
from .views import UserAPIView
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('', UserAPIView.as_view(), name='user-post'),
]