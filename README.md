# Installation 

Commencer par créer un environnment virtuel 

```bash
python3 -m venv myvenv
```

Lancer l'environnement virtuel (`source myvenv/bin/activate` sous unix) puis installer les dépendences du projets 

```bash
pip install -r requirements.txt
```

Il reste plus qu'à appliquer les migrations pour avoir une base de donnée en locale 

```bash
python manage.py migrate
```

Il faut créer une secret key pour les cookies, pour cela on peut utiliser un module de django : 
```bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```
une fois générer plus qu'à créer un fichier `.env` dans lequel on met la secret key générée `SECRET_KEY = 'LA SECRET KEY'`

Puis lancer le serveur : 
```bash
python manage.py runserver
```



