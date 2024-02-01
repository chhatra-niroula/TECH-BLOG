from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('content/', views.content, name='content'),
    path('about/', views.about, name='about'),
    path('blog/', views.listblog, name='listblog'),

]