from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import FriendRequest, Message

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['email', 'last_login', 'date_joined', 'groups', 'friends', 'first_name', 'last_name', 'game_name']

class FriendRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendRequest
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'