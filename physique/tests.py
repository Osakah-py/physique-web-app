import requests
from bs4 import BeautifulSoup
from .models import Categorie, Document

response = requests.get('https://physique.mp2i-champo.fr/')

soup = BeautifulSoup(response.text, 'html.parser')

compteur_cat = 0
compteur_doc = 0
for heading in soup.find_all("h2"):  # trouver les separateurs, ici les h2
    
    # On creer ou modifie la categorie
    compteur_cat += 1
    cat, created = Categorie.objects.get_or_create(pk=compteur_cat)
    print("****\n On a ajouté la categorie : " + heading.get_text() + "****")

    # On creer ou modifie tout les documents de cette categorie
    for sibling in heading.find_next_siblings():
        if sibling.name == "h2":  # on s'arrete au prochain h2
            break
        elif sibling.name == "p": # on s'interresse que au balise p
            compteur_doc += 1
            text = sibling.get_text()
            text = text.replace("\n","")
            # On lui attribue son nom, le lien ou il se trouve ainsi que sa categorie
            lien, created = Document.objects.get_or_create(pk=compteur_doc)
            lien.title = text
            lien.categorie = cat
            print("On ajoute :" + text)
            
            #le lien (on traite le cas ou il existe pas)
            link = sibling.find('a')
            if link:
                href = link.get('href')
                lien.link = href
            else:
                lien.link = "404"
            
            # on sauvegarde
            lien.save()