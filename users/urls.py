from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.index, name='users-index'),
    path('register/', views.UserRegistrationView.as_view()),
    path('login/', obtain_auth_token)
]