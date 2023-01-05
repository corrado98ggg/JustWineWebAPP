from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import UserManager


# Create your models here.

def randomString():
    um = UserManager()
    return( um.make_random_password( length=25 ) )

class forum(models.Model):
    nome=models.CharField(max_length=30, default="anonimo")
    email=models.EmailField(null=True)
    topic=models.CharField(max_length=230)
    descrizione = models.TextField(blank=True)
    slug_title = models.SlugField(default=randomString)
    

    def __str__(self):
        return self.topic


class Discussione(models.Model):
    forum = models.ForeignKey(forum, blank=True, on_delete=models.CASCADE, default="anonimo")
    nome_forum_associato = models.CharField(max_length=30, default="anonimo") 
    discuss = models.TextField()
    username = models.CharField(default="anonimo", max_length=30)


    def __str__(self):
        return self.nome_forum_associato
 

class Partecipa_vero(models.Model):
    nome_topic_forum = models.ForeignKey(forum, blank=True, on_delete=models.CASCADE, default="ciao")
    partecipa = models.BooleanField()
    user_che_partecipa = models.CharField(max_length=50, default="anonimo")

    def __str__(self):
        return self.user_che_partecipa  