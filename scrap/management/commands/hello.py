from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    args = ''
    help = 'affiche Hello worlds !'
    
    def handle(self, *args, **options):
        print('Hello, world!')