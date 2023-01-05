from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"), #mettendo '' vuoto stiamo già dicendo che sarà a /malattie 
]
