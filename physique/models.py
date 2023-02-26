from django.conf import settings
from django.db import models
from django.utils import timezone


class Categorie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(default=' ')
    libele = models.CharField(max_length=200, help_text="Petit texte d'entête du tableau", default='Nom')
    corrections = models.BooleanField(default=False, help_text="À cocher si cette categorie possède des corrections")

    def __str__(self):
        return self.title

class Document(models.Model):
    title = models.CharField(max_length=200)
    link = models.CharField(blank=True, max_length=200, help_text="Au format 'fichier.pdf' ")
    categorie = models.ForeignKey(Categorie, null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title