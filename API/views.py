from django.shortcuts import HttpResponse, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.permissions import IsAuthenticated
from .serilalizers import UserSerializer, FriendRequestSerializer, MessageSerializer
from django.contrib.auth import get_user_model
from .models import FriendRequest, Message

def index(request):
    return HttpResponse('<h1>Welcome to the api...</h1>')


class UserList(APIView):
    # permission_classes = [IsAuthenticated,]
    UserModel = get_user_model()
    def get(self, request, format=None):
        users = self.UserModel.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

class UserDetail(APIView):
    UserModel = get_user_model()
    def get(self, request, username, form=None):
        user = get_object_or_404(self.UserModel, username = username)
        serializer = UserSerializer(user)
        return Response(serializer.data)

class GetFriendRequests(APIView):
    UserModel = get_user_model()
    def get(self, request, username, format=None):
        request_to = self.UserModel.objects.get(username=username)
        friend_requests = FriendRequest.objects.filter(to_user = request_to)
        serializer = FriendRequestSerializer(friend_requests, many=True)
        for item in serializer.data:
            from_user = self.UserModel.objects.get(id=item['from_user'])
            item['request_name'] = f'{from_user.first_name} {from_user.last_name}'
        return Response(serializer.data)

class GetFriends(APIView):
    UserModel = get_user_model()
    def get(self, request, id, format=None):
        user = get_object_or_404(self.UserModel, id=id)
        serializer = UserSerializer(user)
        friend_list = []
        for friend_id in serializer.data['friends']:
            friend = get_object_or_404(self.UserModel, id=friend_id)
            friend_list.append({
                "id":friend_id,
                "first_name": friend.first_name,
                "last_name": friend.last_name
            })
        return Response(friend_list)

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
        friend_request = get_object_or_404(FriendRequest, id=id)
        serializer = FriendRequestSerializer(friend_request)
        return Response(serializer.data)
    
    def patch(self, request, id, form=None):
        friend_request = get_object_or_404(FriendRequest, id=id)
        to_user = get_object_or_404(self.UserModel, id = request.data['to_user'])
        from_user = get_object_or_404(self.UserModel, id = request.data['from_user'])
        serializer = FriendRequestSerializer(friend_request, data=request.data, partial=True)
        if serializer.is_valid():
            if request.data['accepted']:
                to_user.friends.add(from_user)
                from_user.friends.add(to_user)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MessageList(APIView):
    UserModel = get_user_model()

    def get(self, request, form=None):
        messages = Message.objects.all()
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)

    def post(self, request, form=None):
        # message = request.data['message']
        # to_user = get_object_or_404(self.UserModel, id = request.data['to_user'])
        # from_user = get_object_or_404(self.UserModel, id = request.data['from_user'])
        # data = {
        #     "to_user":to_user,
        #     "from_user":from_user,
        #     "message": message
        # }
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)