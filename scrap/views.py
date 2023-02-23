from django.shortcuts import render
from .models import Categorie, Document
import itertools

"""
idée a mettre en place : 
plutot que renvoyer deux dictionnaires, renvoyer un dictionnaire de dictionnaires tel que :

categories = {
    <Category : 'DS'>:
	{'documents': [DS1,DS2], 'corrections': [correction DS 1, correction DS 2]},
    <Category : 'TD'>:
	{'documents': [TD1,TD2,TD3], 'corrections': [correction TD 1, correction TD 2]},
}

Pour l'integrer a notre template on s'aidera de la balise empty : https://docs.djangoproject.com/fr/4.1/ref/templates/builtins/#for-empty
et regroup ? https://docs.djangoproject.com/fr/4.1/ref/templates/builtins/#regroup

autre option qui peut etre plus simple peut etre dans un template : 
categories = {
    <Category : 'DS'>:
	{[DS1,DS2],[correction DS 1, correction DS 2]},
    <Category : 'TD'>:
	{[TD1,TD2,TD3],[correction TD 1, correction TD 2]},
}
qui donnera quelque chose comme : 

{% for cat, listes in categories %}

   {% for document, correction in listes %}
     Doc : {{ document }} Correction : {{ correction }}
   {% endfor %}

{% endfor %}
"""

def accueil(request):
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
            elif "bonus" in documents[i].title or ("13" in documents[i].title and not("13" in correction[i].title)):
                documents_by_category[category].append((documents[i], "N/A"))
            else : 
                documents_by_category[category].append((documents[i], correction[c]))
                c += 1
            

            # documents_by_category[category] = itertools.zip_longest(documents,correction,fillvalue='N/A')
    return render(request, 'home.html', {'documents_by_category': documents_by_category})

def google(request):
    return render(request, 'google311f29b3ed4bd3be.html')