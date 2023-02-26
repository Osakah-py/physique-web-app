from django.core.management.base import BaseCommand, CommandError
import requests
from bs4 import BeautifulSoup
from physique.models import Categorie, Document

class Command(BaseCommand):
    args = ''
    help = 'met a jour la base de donnee'
    
    def handle(self, *args, **options):
        
        headers = {
        "Accept-Language" : "en-US,en;q=0.5",
        "User-Agent": "Defined",
        }
        proxies = {
        "http": "http://185.15.172.212:3128",
        "https": "http://185.15.172.212:3128",
        }

        response = requests.get('https://physique.mp2i-champo.fr/', headers=headers)

        soup = BeautifulSoup(response.text, 'html.parser')

        compteur_cat = 0
        compteur_doc = 0
        
        for heading in soup.find_all("h2"):  # trouver les separateurs, ici les h2
        # On creer ou modifie la categorie
            compteur_cat += 1
            cat, created = Categorie.objects.get_or_create(pk=compteur_cat)
            nom_de_cat = heading.get_text()
            nom_de_cat = nom_de_cat.replace("\n","")
            cat.title = nom_de_cat
            cat.save()
            print("****\n On a ajouté la categorie : " + cat.title + "****")
            tampon = [] # Pour sauvegarder dans le bon ordre
        # On creer ou modifie tout les documents de cette categorie
            for sibling in heading.find_next_siblings():
                if sibling.name == "h2":  # on s'arrete au prochain h2
                    while tampon:
                        compteur_doc += 1
                        t, l = tampon.pop()
                        lien, created = Document.objects.get_or_create(pk=compteur_doc)
                        # On lui attribue son nom, le lien ou il se trouve ainsi que sa categorie
                        lien.title = t
                        lien.categorie = cat
                        lien.link = l
                        lien.save()
                    break
                elif sibling.name == "p": # on s'interresse que au balise p
                    for balise in sibling: # on cherche tout les liens 
                        if balise.name == "a" and balise.get_text() != " annexe ":
                            text = balise.get_text()
                            text = text.replace("\n","")
                            print("On ajoute :" + balise.get_text())
                            href = balise.get('href')
                            tampon.append((text, href))
