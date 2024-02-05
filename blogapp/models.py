import datetime
from django.db import models


# Create your models here.

class BlogUser(models.Model):
    blog_full_Name = models.CharField(max_length=50)
    blog_user_email = models.CharField(max_length=100)
    blog_username = models.CharField(max_length=50, null=False)
    blog_user_role = models.CharField(max_length=50, default="normal")
    blog_user_created = models.DateTimeField(auto_now_add=True)
    blog_user_isactive = models.BooleanField(default=False)
    blog_user_modified = models.DateTimeField(blank=True, null=True)
    blog_user_title = models.CharField(max_length=250,null=False, default="Graphics Designer | Programmer")

    def __str__(self):
        # return "Username: "+self.blog_username+", "+self.blog_user_title
        return self.blog_full_Name


class BlogPost(models.Model):
    blog_created_by = models.ForeignKey(BlogUser, on_delete=models.CASCADE )
    blog_title = models.CharField(max_length=100)
    blog_description = models.TextField()
    blog_is_active = models.CharField(max_length=50, default="normal")
    blog_published_date = models.DateTimeField(auto_now_add=True)
    blog_modified = models.DateTimeField(blank=True, null=True)
    blog_img = models.ImageField(upload_to='images/', default="images/no-image.jpg")

    def __str__(self):
        return self.blog_title
    
    def img_url(self):
        if self.blog_img and hasattr(self.blog_img, 'url'):
            return self.blog_img.url


