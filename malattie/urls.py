from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.malattie, name="malattia"), #mettendo '' vuoto stiamo già dicendo che sarà a /malattie 
    path('nuova_malattia/', views.inserisci_nuova_malattia, name="inserisci_nuova_malattia")
]
