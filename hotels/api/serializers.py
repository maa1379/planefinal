from rest_framework import serializers

from profiles.models import Profile


class LoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128)


class PasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField(max_length=128)
    new_password = serializers.CharField(max_length=128)


class UserUpdateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Profile
		fields = ['first_name', 'last_name', 'email','birthday']



class RegisterUserSerializer(serializers.Serializer):
	phone_number = serializers.CharField(max_length=12, required=True)
	password = serializers.CharField(max_length=15, required=True)



class RegisterVerifiedSerializer(serializers.Serializer):
	code = serializers.CharField(max_length=4)
	phone_number = serializers.CharField(max_length=12)
	password=serializers.CharField(max_length=12)