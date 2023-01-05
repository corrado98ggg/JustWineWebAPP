from django.db import models
from xml.parsers.expat import model

# Create your models here.
#qui creiamo la tabella nel database della malattia

class home_notizia(models.Model):

    nome_notizia = models.TextField()
    descrizione = models.TextField()

    def __str__(self):
        return self.nome_notizia