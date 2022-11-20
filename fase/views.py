from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from six import text_type

from .serializers import *
from back.models import *
from .models import *
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
    pagination_class = PagEvents
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        district = self.request.GET.get('district')
        if district:
            return Events.objects.filter(district__name=district, status='A')
        else:
            return Events.objects.filter(status='A')


class ListAdminEvent(generics.ListAPIView):
    serializer_class = AdminEventSer
    pagination_class = PagEvents

    def get_queryset(self):
        choice = self.request.GET.get('choice')
        return Events.objects.filter(status=choice)


class NumberLikes(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        ob = Likes.objects.filter(user=request.user)
        context = []
        if len(ob) == 1:
            context.append(ob[0].event.id)
        else:
            for i in ob:
                context.append(i.event.id)

        return Response({
            'likes': context,
            'status': 'true'
        })


class CreatComments(generics.CreateAPIView):
    serializer_class = CommentsSer
    queryset = Comments.objects.all()
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class ListComments(generics.ListAPIView):
    serializer_class = CommentsSer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        pk = self.kwargs['pk']
        ob = Events.objects.get(pk=pk).comments_set.all()
        return ob


class AddLike(generics.UpdateAPIView):
    serializer_class = EventSer
    queryset = Events.objects.all()
    permission_classes = (IsAuthenticated,)

    def put(self, request, *args, **kwargs):
        pk = kwargs['pk']
        user = self.request.user
        ob = Events.objects.get(pk=pk)
        Likes.objects.create(user=user, event=ob)
        ob.like += 1
        ob.save()
        return Response({
            'much': ob.like,
            'status': 'true'
        })


class CreateUser(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class PhotoEvent(generics.CreateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSer
    permission_classes = (IsAuthenticated,)


def create(self, request, *args, **kwargs):
    response = super().create(request, *args, **kwargs)
    return Response({
        'id': response.data['id']
    })
