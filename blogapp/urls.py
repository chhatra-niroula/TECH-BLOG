from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('content/', views.content, name='content'),
    path('about/', views.about, name='about'),
    path('bloghome/', views.bloghome, name='bloghome'),
    path('listblog/<int:id>', views.readblog, name='listblog'),

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)