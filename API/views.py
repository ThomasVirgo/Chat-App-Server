from django.shortcuts import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serilalizers import UserSerializer
from django.conf import settings
from django.contrib.auth import get_user_model

def index(request):
    return HttpResponse('<h1>Welcome to the api...</h1>')


class UserList(APIView):
    # permission_classes = [IsAuthenticated,]
    UserModel = get_user_model()
    def get(self, request, format=None):
        restaurants = self.UserModel.objects.all()
        serializer = UserSerializer(restaurants, many=True)
        return Response(serializer.data)

    