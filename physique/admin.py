from django.contrib import admin
from .models import Categorie, Document, Statistiques

from django.contrib import admin
from .models import Document, Categorie

# DOCUMENT MODEL 
@admin.action(description="Rendre visible")
def make_visible(modeladmin, request, queryset):
    queryset.update(visible=True)

@admin.action(description="Masquer")
def make_hidden(modeladmin, request, queryset):
    queryset.update(visible=False)

class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'categorie', 'visible')
    list_filter = ('categorie',)
    actions = [make_visible, make_hidden]

# CATEGORIE MODEL
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'colonnes')
    exclude = ('colonnes',)

#### AJOUT FINAL ###
admin.site.register(Document, DocumentAdmin)
admin.site.register(Categorie, CategorieAdmin)

# git reset --hard HEAD