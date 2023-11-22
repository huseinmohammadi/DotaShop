from rest_framework import serializers
from user.models import User
import re


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ['password']


class UserRegisterSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    email = serializers.CharField()
    password = serializers.CharField()
    password_repeat = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    national_code = serializers.CharField(required=False)
    father_name = serializers.CharField(required=False)
    birth_date = serializers.CharField(required=False)

    def validate(self, validated_data):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if User.objects.filter(phone_number=validated_data['phone_number']).exists():
            raise serializers.ValidationError({'message': 'this phone number valid !!!'})
        if User.objects.filter(national_code=validated_data['national_code']).exists():
            raise serializers.ValidationError({'message': 'this national code valid !!!'})
        if User.objects.filter(email=validated_data['email']).exists():
            raise serializers.ValidationError({'message': 'this email valid !!!'})
        if not re.fullmatch(regex, validated_data['email']):
            raise serializers.ValidationError({'message': 'The email structure is incorrect !!!'})
        if not User.check_phone_number(validated_data['phone_number']):
            raise serializers.ValidationError({'message': 'Your phone number structure is incorrect !!!'})
        return validated_data

    def create(self, validated_data):
        if validated_data['password'] != validated_data['password_repeat']:
            raise serializers.ValidationError({'message': 'password and password repeat is not equal !!!'})
        del validated_data['password_repeat']
        return User.objects.create(**validated_data)


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    code = serializers.CharField()

    def create(self, validated_data):
        user = User.objects.filter(username=validated_data['username'])
        if not user.exists():
            return {'message': 'username invalid !!!', 'status': False}
        return {"status": True, "user": user[0]}
