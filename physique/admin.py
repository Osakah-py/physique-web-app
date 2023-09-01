from django.contrib import admin
from .models import Categorie, Document, Statistiques

from django.contrib import admin
from .models import Document, Categorie

class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'categorie')
    list_filter = ('categorie',)

class CategorieAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'colonnes')
    exclude = ('colonnes',)

admin.site.register(Document, DocumentAdmin)
admin.site.register(Categorie, CategorieAdmin)

# git reset --hard HEAD