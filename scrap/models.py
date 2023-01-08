from django.conf import settings
from django.db import models
from django.utils import timezone


class Categorie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(default=' ')
    libele = models.CharField(max_length=200, default='Nom')
    last_update = models.DateTimeField(blank=True, null=True)
    corrections = models.BooleanField(default=False)
    def publish(self):
        self.last_update = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Document(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField(blank=True)
    categorie = models.ForeignKey(Categorie, null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.title