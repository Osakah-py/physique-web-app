from django.core.management.base import BaseCommand, CommandError
from scrap.models import Categorie, Document

class Command(BaseCommand):
    args = ''
    help = 'affiche Hello worlds !'
    
    def handle(self, *args, **options):
        documents_by_category = {}
        correction_by_category ={}

        categories = Categorie.objects.order_by('pk')
        for category in categories:
            if category.corrections:
                correction = Document.objects.filter(categorie=category, title__icontains='correction')
                correction_by_category[category] = correction
                documents = Document.objects.filter(categorie=category).exclude(title__icontains='correction')
                documents_by_category[category] = documents
            else:
                documents = Document.objects.filter(categorie = category)
                documents_by_category[category] = documents
        print(documents_by_category)
        print(correction_by_category)