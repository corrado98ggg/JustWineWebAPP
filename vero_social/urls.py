from django.contrib import admin
from django.urls import path
from .views import inserisci_nuovo_post, social, like_post, who_likes


urlpatterns = [
    path('', social, name="social"), #mettendo '' vuoto stiamo già dicendo che sarà a /malattie
    path('like/', like_post, name="like-post"),
    path('like/<slug:slug>/', who_likes, name="who_likes"), #mettendo '' vuoto stiamo già dicendo che sarà a /malattie

]