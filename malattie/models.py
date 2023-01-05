from audioop import reverse
from unittest.util import _MAX_LENGTH
from xml.parsers.expat import model
from django.db import models

# Create your models here.
# qui creiamo la tabella nel database della malattia


class Malattia(models.Model):

    nome_malattia = models.TextField()
    descrizione = models.TextField()
    sintomi_riassunti = models.TextField()
    difesa = models.TextField()
    immagine = models.ImageField()

    def __str__(self):
        return self.nome_malattia
