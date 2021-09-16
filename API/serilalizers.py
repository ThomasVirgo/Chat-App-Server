from rest_framework import serializers
from django.conf import settings

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = ['id', 'email', 'last_login', 'date_joined', 'groups']
