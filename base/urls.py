from django.contrib import admin
from django.urls import path
from .views import bot, home
from . import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('resumebot', views.bot, name="bot"), 
    path('', views.home, name="home")
]