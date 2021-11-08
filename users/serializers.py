from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserRegistrationSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)
    password_confirmation = serializers.CharField(write_only=True)
    UserModel = get_user_model()

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password', 'password_confirmation', 'first_name', 'last_name', 'game_name')
        write_only_fields = ('password', 'password_confirmation')

    def create(self, validated_data):
        user = self.UserModel.objects.create(
            username=validated_data['username'], email=validated_data['email'], first_name=validated_data['first_name'], last_name=validated_data['last_name'], game_name=validated_data['game_name']
        )
        password=validated_data['password']
        password_confirmation=validated_data['password_confirmation']

        if password != password_confirmation:
            raise serializers.ValidationError({'password': 'Passwords must match.'}) 
        user.set_password(password)
        user.save()

        return user

class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    password_confirmation = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = get_user_model()
        fields = ('old_password', 'password', 'password_confirmation')

    def get_user(self):
        request = self.context
        return request.user

    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirmation']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def validate_old_password(self, value):
        user = self.get_user()
        print('validating old password...')
        if not user.check_password(value):
            raise serializers.ValidationError({"old_password": "Old password is not correct"})
        return value

    def save(self):
        user = self.get_user()
        user.set_password(self.validated_data['password'])
        user.save()
        return user