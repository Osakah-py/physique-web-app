from django.shortcuts import render
from .models import Categorie, Document

def main(request):
    admin_view = request.COOKIES.get('admin_view') == 'True'
    documents_by_category = {}
    categories = Categorie.objects.order_by('pk')
    admin_view = request.COOKIES.get('admin_view') == 'True'

    for category in categories:
        if request.user.is_authenticated and admin_view:
            correction = list(Document.objects.filter(categorie=category, title__icontains='correction').order_by('-pk'))
            documents = list(Document.objects.filter(categorie=category).exclude(title__icontains='correction').order_by('-pk'))
        else: 
            correction = list(Document.objects.filter(categorie=category, visible=True, title__icontains='correction').order_by('-pk'))
            documents = list(Document.objects.filter(categorie=category, visible = True).exclude(title__icontains='correction').order_by('-pk'))
        
        documents_by_category[category] = []
        
        while documents != []:
            curr_doc = documents.pop()
            if correction == [] or "bonus" in curr_doc.title:
                documents_by_category[category].append((curr_doc, "N/A"))
            else:
                curr_corr = correction.pop()
                documents_by_category[category].append((curr_doc, curr_corr))

        documents_by_category[category] = documents_by_category[category][::-1]
            
    return render(request, 'main.html', {'documents_by_category': documents_by_category, 'admin_view':admin_view})