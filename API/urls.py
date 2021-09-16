from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='api-index'),
    path('users', views.UserList.as_view(), name='user-list')
]