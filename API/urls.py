from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='api-index'),
    path('users', views.UserList.as_view(), name='user-list'),
    path('users/<str:username>', views.UserDetail.as_view(), name='user-detail'),
    path('friend-requests/<str:username>', views.GetFriendRequests.as_view(), name='get-friend-requests'),
    path('friend-requests', views.FriendRequestList.as_view(), name='friend-request-list'),
    path('friend-request/<int:id>', views.FriendRequestDetail.as_view(), name='friend-request-detail'),
]