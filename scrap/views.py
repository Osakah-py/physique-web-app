from django.shortcuts import render
from .models import Categorie, Document

def accueil(request):
    documents_by_category = {}
    categories = Categorie.objects.order_by('pk')
    for category in categories:
        documents = Document.objects.filter(categorie = category)
        documents_by_category[category] = documents

    return render(request, 'home.html', {'documents_by_category': documents_by_category})
