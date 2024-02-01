from django.contrib import admin
from blogapp.models import BlogUser, BlogPost

# Register your models here.

admin.site.register(BlogUser)
admin.site.register(BlogPost)