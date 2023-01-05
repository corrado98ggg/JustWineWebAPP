from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.forum_home, name="forum"), #mettendo '' vuoto stiamo già dicendo che sarà a /forum
]
