from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import FriendRequest

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username', 'id', 'email', 'last_login', 'date_joined', 'groups', 'friends', 'first_name', 'last_name']

class FriendRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendRequest
        fields = '__all__'