from django.shortcuts import HttpResponse

def home(request):
    return HttpResponse('<h1>Welcome to the chat app server...</h1>')
