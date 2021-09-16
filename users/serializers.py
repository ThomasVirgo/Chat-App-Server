from rest_framework import serializers
from django.conf import settings
from django.contrib.auth.models import User


class UserRegistrationSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)
    password_confirmation = serializers.CharField(write_only=True)

    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = ('email', 'password', 'password_confirmation')
        write_only_fields = ('password', 'password_confirmation')

    def create(self, validated_data):
        user = settings.AUTH_USER_MODEL.objects.create(
            email=validated_data['email']
        )
        password=validated_data['password']
        password_confirmation=validated_data['password_confirmation']

        if password != password_confirmation:
            raise serializers.ValidationError({'password': 'Passwords must match.'}) 
        user.set_password(password)
        user.save()

        return user