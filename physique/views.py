from django.shortcuts import render, redirect
from .models import Categorie, Document, Statistiques
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.core.exceptions import PermissionDenied
from django.core.files.storage import FileSystemStorage

# Page principale ou tous les documents sont affichés
def accueil(request):
    documents_by_category = {}

    categories = Categorie.objects.order_by('pk')
    for category in categories:
        start = category.nombre_affichage
        documents = Document.objects.filter(categorie=category).order_by('-pk')[:start]

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
def more_ajax(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    if is_ajax and request.method == 'GET':
        cat = request.GET.get("categorie", None)
        categorie = Categorie.objects.get(pk=cat)
        start = categorie.nombre_affichage
        documents = list(Document.objects.filter(categorie=categorie).order_by('-pk')[start:].values('title','fichiers'))
        return JsonResponse({'documents': documents})
    else:
        return HttpResponseBadRequest('Invalid request')

def add_ajax(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    if is_ajax and request.method == 'POST':
        
        # on récupère les données de l'unpload
        title = request.POST.get('title','')
        cat = request.POST.get('cat', '')
        nbfiles = request.POST.get('nbfiles', '')
        categorie = Categorie.objects.get(pk=cat)
        
        # récuperation des fichiers
        fss = FileSystemStorage()
        url_list = ""
        for field_name, file_data in request.FILES.items():
        # field_name est le nom du champ de fichier
        # file_data est un objet UploadedFile contenant les informations sur le fichier
            print("--------------")
        # infos du fichier
            file_name = file_data.name
            file_size = file_data.size
            content_type = file_data.content_type

        # pour les logs
            print(f"Nom du fichier: {file_name}")
            print(f"Taille du fichier: {file_size} octets")
            print(f"Type de contenu: {content_type}")

            filename = fss.save(file_name, file_data)
            url_list += fss.url(filename)

        print("--------------")
        return JsonResponse({'pk': cat, 'title': title})
    else:
        return HttpResponseBadRequest('Invalid request')

# pour traquer les ressources consultées
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