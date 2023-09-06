from rest_framework import serializers
from .models import UserDownload


class UsersSerializers(serializers.ModelSerializer):
    name = serializers.CharField(required=True, max_length=100)
    company = serializers.CharField(required=True, max_length=100)
    position = serializers.CharField(required=True, max_length=100)
    phone = serializers.CharField(required=True, max_length=20)
    country = serializers.CharField(required=True, max_length=50)
    class Meta:
        model = UserDownload
        fields = [
            'name',
            'company',
            'position',
            'phone',
            'country',
        ]
        extra_kwargs = {
            'name': {'required': True , 'error_messages': {'required': 'Please enter your name'}},
            'company': {'required': True, 'error_messages': {'required': 'Please enter your company'},},
            'position': {'required': True, 'error_messages': {'required': 'Please enter your position'},},
            'phone': {'required': True , 'error_messages': {'required': 'Please enter your phone number'}},
            'country': {'required': True, 'error_messages': {'required': 'Please enter your country'},},
        }