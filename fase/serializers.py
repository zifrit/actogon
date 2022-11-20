from rest_framework import serializers
from back.models import *
from .models import *


class EventSer(serializers.ModelSerializer):
    like = serializers.CharField(read_only=True)
    photo = serializers.CharField(read_only=True)

    class Meta:
        model = Events
        exclude = ['status']


class AdminEventSer(serializers.ModelSerializer):
    photo = serializers.CharField(read_only=True)

    class Meta:
        model = Events
        fields = '__all__'


class CommentsSer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        exclude = ['user']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "username", "password"]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.is_active = True
        user.save()
        return user


class PhotoSer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'
