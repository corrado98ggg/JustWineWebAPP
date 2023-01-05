from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.contattaci, name="contattaci"), #mettendo '' vuoto stiamo già dicendo che sarà a /contattaci 
]
