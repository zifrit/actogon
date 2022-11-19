from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from six import text_type

from .serializers import *
from .models import *
from back.models import *
from rest_framework import generics
from rest_framework.views import APIView


class MyTokenObtainSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        # data = super(TokenObtainPairSerializer, self).validate(attrs)
        # print(attrs['username'])
        data = super(TokenObtainPairSerializer, self).validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = text_type(refresh)
        if self.user.is_superuser:
            new_token = refresh.access_token
            data['access'] = text_type(new_token)
        else:
            data['access'] = text_type(refresh.access_token)

        return data


class MyTokenObtainView(TokenObtainPairView):
    serializer_class = MyTokenObtainSerializer


class CreatListEvent(generics.ListCreateAPIView):
    serializer_class = EventSer
    queryset = Events.objects.all()


class CreatListComments(generics.ListCreateAPIView):
    serializer_class = CommentsSer
    queryset = Comments.objects.all()
