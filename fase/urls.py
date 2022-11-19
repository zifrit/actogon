from django.urls import path, include
from .views import *

urlpatterns = [
    path('events/', CreatListEvent.as_view(), name='event'),
    path('comments/<int:pk>/', ListComments.as_view(), name='list_comments'),
    path('comments/', CreatComments.as_view(), name='create_comments'),
    path('add_like/<int:pk>/', AddLike.as_view(), name='add_like'),
    path('likes/', NumberLikes.as_view(), name='likes'),
]
