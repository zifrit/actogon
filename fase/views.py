from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
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


class PagEvents(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'much_page_size'
    max_page_size = 10


class CreatListEvent(generics.ListCreateAPIView):
    serializer_class = EventSer
    queryset = Events.objects.all()
    pagination_class = PagEvents


class CreatComments(generics.CreateAPIView):
    serializer_class = CommentsSer
    queryset = Comments.objects.all()


class ListComments(generics.ListAPIView):
    serializer_class = CommentsSer

    def get_queryset(self):
        pk = self.kwargs['pk']
        ob = Events.objects.get(pk=pk).comments_set.all()
        return ob


class AddLike(generics.UpdateAPIView):
    serializer_class = EventSer
    queryset = Events.objects.all()

    def put(self, request, *args, **kwargs):
        pk = kwargs['pk']
        ob = Events.objects.get(pk=pk)
        ob.like += 1
        ob.save()
        return Response({
            'much': ob.like,
            'status': 'true'
        })
