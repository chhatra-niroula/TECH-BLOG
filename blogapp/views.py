from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "home.html")


def content(request):
    return render(request, "content.html")


def about(request):
    return render(request, "about.html")


def listblog(request):
    return render(request, "bloglist.html")