from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    response = "hello world"
    return HttpResponse(response)