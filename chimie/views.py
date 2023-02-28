from django.shortcuts import render
from .models import Categorie, Document

def main(request):
   
    documents_by_category = {}
    categories = Categorie.objects.order_by('pk')

    for category in categories:
        correction = Document.objects.filter(categorie=category, title__icontains='correction').order_by('-pk')
        documents = Document.objects.filter(categorie=category).exclude(title__icontains='correction').order_by('-pk')
        l_doc = len(documents)
        l_corr = len(correction)
        c = 0
        documents_by_category[category] = []
        
        for i in range(l_doc):
            if c >= l_corr: 
                documents_by_category[category].append((documents[i], "N/A"))
            elif "bonus" in documents[i].title or ("14" in documents[i].title and not("14" in correction[i].title)):
                documents_by_category[category].append((documents[i], "N/A"))
            else : 
                documents_by_category[category].append((documents[i], correction[c]))
                c += 1
            
    return render(request, 'main.html', {'documents_by_category': documents_by_category})
