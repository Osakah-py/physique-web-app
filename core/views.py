from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.core.files.storage import FileSystemStorage
from physique.models import Categorie as phy_cat
from chimie.models import Categorie as chi_cat

def add_ajax(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    if is_ajax and request.method == 'POST':
        
        # on récupère les données de l'unpload
        title = request.POST.get('title','')
        cat = request.POST.get('cat', '')
        nbfiles = request.POST.get('nbfiles', '')
        app = request.POST.get('app', '')
        print(app)
        if app == "chimie":
            categorie = chi_cat.objects.get(pk=cat)
        else:
            categorie = phy_cat.objects.get(pk=cat)
        
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
            print(f"Categorie : {categorie.title}")
            print(f"Nom du fichier: {file_name}")
            print(f"Taille du fichier: {file_size} octets")
            print(f"Type de contenu: {content_type}")

            filename = fss.save(file_name, file_data)
            url_list += fss.url(filename)

        print("--------------")
        return JsonResponse({'pk': cat, 'title': title})
    else:
        return HttpResponseBadRequest('Invalid request')

def more_ajax(request):
    return HttpResponseBadRequest('Invalid request')