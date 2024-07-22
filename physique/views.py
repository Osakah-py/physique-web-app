from django.shortcuts import render, redirect
from .models import Categorie, Document, Statistiques
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.core.exceptions import PermissionDenied

# Page principale ou tous les documents sont affichés
def accueil(request):
    documents_by_category = {}

    categories = Categorie.objects.order_by('pk')
    for category in categories:
        start = category.nombre_affichage

        if request.user.is_authenticated:
            documents = Document.objects.filter(categorie=category).order_by('-pk')[:start]
            documents_by_category[category] = documents
        else: 
            documents = Document.objects.filter(categorie=category, visible=True).order_by('-pk')[:start]
            documents_by_category[category] = documents 

    return render(request, 'home.html', {'documents_by_category': documents_by_category})

# pour le google bot (indexation moteur de recherche)
def google(request):
    return render(request, 'google311f29b3ed4bd3be.html')

#erreur 404
def handler404 (request, exception=None):
    return render(request, '404.html', {'er404':404})

#erreur 403
def handler403 (request, exception=None):
    return HttpResponse("Erreur 403 : Vous n'avez pas les permissions pour voir cette page.")

# pour tester js/html (oui je sais c moche en production)
def test(request):
    return render(request, 'test.html')

# Pour le "afficher +"
def test_ajax(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    if is_ajax and request.method == 'GET':
        cat = request.GET.get("categorie", None)
        categorie = Categorie.objects.get(pk=cat)
        start = categorie.nombre_affichage
        documents = []
        if request.user.is_authenticated:
            documents = list(Document.objects.filter(categorie=categorie).order_by('-pk')[start:].values('title','fichiers','visible'))
        else: 
            documents = list(Document.objects.filter(categorie=categorie, visible=True).order_by('-pk')[start:].values('title','fichiers','visible'))
        return JsonResponse({'documents': documents})
    else:
        return HttpResponseBadRequest('Invalid request')

def acces_ressource (request):
    fichier = request.GET['fichier']
    cat = request.GET['cat']

    url = "https://physique.mp2i-champo.fr/" + fichier

    # on enregistre le telechargement 
    stat, created = Statistiques.objects.get_or_create(nom=fichier)
    if created:
        stat.nom = fichier
        stat.categorie = Categorie.objects.get(pk=cat)
    stat.telechargements_cette_semaine += 1
    stat.telechargements_global += 1
    stat.save()

    return redirect(url)

def stats(request):
    if request.user.is_authenticated:
        telechargements = Statistiques.objects.order_by('-pk')   
        return render(request, 'stats.html', {'telechargements': telechargements})
    else:
        raise PermissionDenied() 