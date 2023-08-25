from django.core.management.base import BaseCommand, CommandError
from physique.models import Statistiques
import datetime

class Command(BaseCommand):
    args = ''
    help = 'reset les enregistrements de statistiques pour la semaine en cours'
    
    def handle(self, *args, **options):
        today = datetime.date.today()
        weekday = today.weekday()
        if (weekday == 0):
             # On reset la stat de semaine
             tout = Statistiques.objects.all()
             for stat in tout:
                 stat.telechargements_semaine_derniere = stat.telechargements_cette_semaine
                 stat.telechargements_cette_semaine = 0
                 stat.save()
        else:
            print("rien aujourd'hui")