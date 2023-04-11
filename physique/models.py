from django.conf import settings
from django.db import models
from django.utils import timezone
from django.dispatch import receiver

class Categorie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(default=' ')
    entetes = models.CharField(max_length=200, help_text="Les entêtes du tableau séparées par des '/' \n Ex: Nom/Fichier/Correction", default='Nom')
    colonnes = models.PositiveIntegerField(default=1 ,help_text="Indiquer le nombre de colonne qu'il y aura (hors celle de numérotation)")
    nombre_affichage = models.PositiveIntegerField(default=20 ,help_text="Corespond au nombre d'éléments qui seront affichés au chargement de la page")

    # permet de calculer le nombre de colonne a chaque enregistrement 
    def publish (self):
        col = self.entetes.count('/')
        self.colonnes = col

    # permet de récupérer les entêtes sous forme de liste
    def get_head (self):
        # print(self.entetes.strip().split('/'))
        return self.entetes.strip().split('/')

    def __str__(self):
        return self.title

class Document(models.Model):
    title = models.CharField(max_length=200)
    fichiers = models.TextField(blank=True, help_text="chaque ligne représente un fichier au format 'fichier.pdf' ")
    categorie = models.ForeignKey(Categorie, null=True, on_delete=models.CASCADE)
    
    # renvoit les liens sous la forme de liste de taille du nombre de colonnes de la Categorie associée
    def split(self):
        c = self.categorie.colonnes
        liste = self.fichiers.strip().split("\n")[0:c] 
        for i in range (0, c-len(liste)):
            liste.append("")
        return liste

    def __str__(self):
        return self.title
    
@receiver (models.signals.pre_save, sender=Categorie)
def cat_pre_save (sender, instance, **kwargs):
    instance.publish()