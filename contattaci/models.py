from django.db import models

# Create your models here.

class contattaci(models.Model):

    nome_da_contattare = models.TextField()
    cognome_da_contattare = models.TextField()
    paese = models.TextField()
    email = models.TextField()
    oggetto = models.TextField()

    def __str__(self):
        return self.name
        
