from rest_framework import serializers
from .models import *


class EventSer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = '__all__'


class CommentsSer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'