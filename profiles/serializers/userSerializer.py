from rest_framework import serializers
from rest_framework.fields import URLField

from profiles.models import User
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes


class CreateUserSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(max_length=30, required=True)
    password = serializers.CharField(min_length=8, max_length=128, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'phone_number', 'device_number')

    def create(self, validated_data):
        user = User.objects.create(
           email=validated_data['email'],
           username=validated_data['username'],
           phone_number=validated_data['phone_number'],
           device_number=validated_data['device_number'],
           is_active = True,
        )
        user.set_password(validated_data['password'])
        user.save()
        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.uuid))
        # user.send_verification_email(uid, token)
        return user


# class UserGetPublicInfosSerializer(serializers.ModelSerializer):
#     skills = GetSkillsSerializer(many=True, read_only=True)
#     client_projects = GetUserProjectsInPublicInfos(many=True, read_only=True)
#     freelancer_projects = GetUserProjectsInPublicInfos(many=True, read_only=True)
#
#     class Meta:
#         model = User
#         fields = ('username', 'first_name', 'last_name', 'title', 'bio', 'date_joined', 'profile_picture', 'avatar',
#                   'university', 'skills', 'client_projects', 'freelancer_projects', 'is_freelancer')
#
#
# class UserGetInitialInfosSerializer(serializers.ModelSerializer):
#     skills = GetSkillsSerializer(many=True, read_only=True)
#     client_projects = GetProjectsSerializer(many=True, read_only=True)
#     freelancer_projects = GetProjectsSerializer(many=True, read_only=True)
#
#     class Meta:
#         model = User
#         fields = ('username', 'first_name', 'last_name', 'email', 'uuid', 'is_active', 'phone_number',
#                   'is_email_verified', 'title', 'bio', 'date_joined', 'profile_picture', 'avatar', 'wish_coins',
#                   'freelancer_rate', 'client_rate', 'freelancer_score', 'client_score', 'job', 'degree', 'university',
#                   'skills', 'client_projects', 'freelancer_projects', 'balance', 'is_freelancer')
#
#
# class UserUpdateInfosSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('title', 'bio', 'job', 'degree', 'university', 'profile_picture')
#
#
