from django.shortcuts import render
from .models import Categorie, Document
from django.http import HttpResponseBadRequest, JsonResponse

def accueil(request):
    documents_by_category = {}

    categories = Categorie.objects.order_by('pk')
    for category in categories:
        start = category.nombre_affichage
        documents = Document.objects.filter(categorie=category).order_by('-pk')[:start]
        l_doc = len(documents)

        documents_by_category[category] = documents
    
    return render(request, 'home.html', {'documents_by_category': documents_by_category})

def google(request):
    return render(request, 'google311f29b3ed4bd3be.html')

def handler404 (request, exception=None):
    return render(request, '404.html', {'er404':404})

def test(request):
    return render(request, 'test.html')

def test_ajax(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    if is_ajax and request.method == 'GET':
        cat = request.GET.get("categorie", None)
        categorie = Categorie.objects.get(pk=cat)
        start = categorie.nombre_affichage
        documents = list(Document.objects.filter(categorie=categorie).order_by('-pk')[start:].values('title','fichiers'))
        return JsonResponse({'documents': documents})
    else:
        return HttpResponseBadRequest('Invalid request')