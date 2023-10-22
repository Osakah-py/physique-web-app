from django.shortcuts import render
from .models import Categorie, Document

# Page principale ou tous les documents sont affichés
def main(request):
    documents_by_category = {}

    categories = Categorie.objects.order_by('pk')
    for category in categories:
        start = category.nombre_affichage
        documents = Document.objects.filter(categorie=category).order_by('-pk')[:start]

        documents_by_category[category] = documents
    
    return render(request, 'main.html', {'documents_by_category': documents_by_category})
