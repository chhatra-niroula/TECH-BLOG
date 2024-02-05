import json
from django.shortcuts import render
from django.http import HttpResponse
from blogapp.models import BlogPost, BlogUser

# Create your views here.
def home(request):
    return render(request, "home.html")


def content(request):
    return render(request, "content.html")


def about(request):
    return render(request, "about.html")


def readblog(request, id):
    # blogdata = BlogPost.objects.all()
    blogdata = BlogPost.objects.get(id=id)
    bloguser = BlogUser.objects.get(id=1)
    
    context = {
        'blogdata': blogdata,
        'bloguser': bloguser,
    }
    print(blogdata.blog_created_by)
    return render(request, "bloglist.html", context)

def bloghome(request):
    blogdata = BlogPost.objects.all()
    context = {
        'blogdata': blogdata,
    }

    return render(request, "blogs_home.html", context)