from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from .views import *

urlpatterns = [
    path('login/', MyTokenObtainView.as_view(), name='get_token'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('events/', CreatListEvent.as_view(), name='event'),
    path('event/<int:pk>/', GetEvent.as_view(), name='event'),
    path('admin_events/', ListAdminEvent.as_view(), name='admin_events'),
    path('add_photo/', PhotoEvent.as_view(), name='photo_events'),
    path('comments/<int:pk>/', ListComments.as_view(), name='list_comments'),
    path('comments/', CreatComments.as_view(), name='create_comments'),
    path('add_like/<int:pk>/', AddLike.as_view(), name='add_like'),
    path('likes/', NumberLikes.as_view(), name='likes'),
    path('create_user/', CreateUser.as_view(), name='create_user'),
]
