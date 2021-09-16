from django.shortcuts import HttpResponse

def index(request):
    return HttpResponse('<h1>Welcome to the api...</h1>')
