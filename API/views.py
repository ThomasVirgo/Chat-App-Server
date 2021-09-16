from django.shortcuts import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .serilalizers import UserSerializer

def index(request):
    return HttpResponse('<h1>Welcome to the api...</h1>')


class UserList(APIView):
    # permission_classes = [IsAuthenticated,]
    def get(self, request, format=None):
        restaurants = User.objects.all()
        serializer = UserSerializer(restaurants, many=True)
        return Response(serializer.data)

    