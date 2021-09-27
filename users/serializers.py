from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserRegistrationSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)
    password_confirmation = serializers.CharField(write_only=True)
    UserModel = get_user_model()

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password', 'password_confirmation', 'first_name', 'last_name')
        write_only_fields = ('password', 'password_confirmation')

    def create(self, validated_data):
        user = self.UserModel.objects.create(
            username=validated_data['username'], email=validated_data['email'], first_name=validated_data['first_name'], last_name=validated_data['last_name']
        )
        password=validated_data['password']
        password_confirmation=validated_data['password_confirmation']

        if password != password_confirmation:
            raise serializers.ValidationError({'password': 'Passwords must match.'}) 
        user.set_password(password)
        user.save()

        return user