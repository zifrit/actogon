from django.urls import path, include
from .views import *

urlpatterns = [
    path('events/', CreatListEvent.as_view(), name='event'),
    path('comments/', CreatListComments.as_view(), name='event')
]
