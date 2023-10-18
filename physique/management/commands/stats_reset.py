from django.core.management.base import BaseCommand, CommandError
from physique.models import Statistiques
import datetime

class Command(BaseCommand):
    args = ''
    help = 'reset les enregistrements de statistiques pour la semaine en cours'

    def handle(self, *args, **options):
        today = datetime.date.today()
        weekday = today.weekday()
        print("Nous sommes le " + str(weekday) + "eme jour de la semaine", flush=True)
        if (weekday == 0):
             # On reset la stat de semaine
             tout = Statistiques.objects.all()
             for stat in tout:
                 stat.telechargements_semaine_derniere = stat.telechargements_cette_semaine
                 stat.telechargements_cette_semaine = 0
                 stat.save()
             print("-> full reset terminé", flush=True)
        else:
            print("-> rien aujourd'hui", flush=True)
