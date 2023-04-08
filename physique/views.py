from django.shortcuts import render
from .models import Categorie, Document
import itertools

def accueil(request):
    documents_by_category = {}

    categories = Categorie.objects.order_by('pk')
    for category in categories:
        documents = Document.objects.filter(categorie=category).order_by('-pk')
        l_doc = len(documents)

        documents_by_category[category] = documents
    
    return render(request, 'home.html', {'documents_by_category': documents_by_category})

def google(request):
    return render(request, 'google311f29b3ed4bd3be.html')

def handler404 (request, exception=None):
    return render(request, '404.html', {'er404':404})