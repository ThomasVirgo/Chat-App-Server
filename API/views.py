from django.shortcuts import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serilalizers import UserSerializer, FriendRequestSerializer
from django.contrib.auth import get_user_model
from .models import FriendRequest

def index(request):
    return HttpResponse('<h1>Welcome to the api...</h1>')


class UserList(APIView):
    # permission_classes = [IsAuthenticated,]
    UserModel = get_user_model()
    def get(self, request, format=None):
        restaurants = self.UserModel.objects.all()
        serializer = UserSerializer(restaurants, many=True)
        return Response(serializer.data)

class GetFriendRequests(APIView):
    UserModel = get_user_model()
    def get(self, request, username, format=None):
        request_to = self.UserModel.objects.filter(username=username)
        friend_requests = FriendRequest.objects.filter(to_user = request_to)
        serializer = FriendRequestSerializer(friend_requests, many=True)
        return Response(serializer.data)

class FriendRequestList(APIView):
    UserModel = get_user_model()

    def get(self, request, form=None):
        friend_requests = FriendRequest.objects.all()
        serializer = FriendRequestSerializer(friend_requests, many=True)
        return Response(serializer.data)

    def post(self, request, form=None):
        to_user_email = request.data['to_user']
        from_user_email = request.data['from_user']
        to_user = self.UserModel.objects.get(username = to_user_email).id
        from_user = self.UserModel.objects.get(username = from_user_email).id
        data = {
            "to_user":to_user,
            "from_user":from_user
        }
        serializer = FriendRequestSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class FriendRequestDetail(APIView):
    UserModel = get_user_model()
    def get(self, request, id, form=None):
        friend_request = FriendRequest.objects.get(id = id)
        serializer = FriendRequestSerializer(friend_request)
        return Response(serializer.data)
