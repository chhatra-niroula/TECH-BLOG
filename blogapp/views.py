import json
from django.shortcuts import render
from django.http import HttpResponse
from blogapp.models import BlogPost

# Create your views here.
def home(request):
    return render(request, "home.html")


def content(request):
    return render(request, "content.html")


def about(request):
    return render(request, "about.html")


def listblog(request):
    blogdata = BlogPost.objects.all()
    data = list(blogdata)
    print(data[0])
    return render(request, "bloglist.html", {'data': data})