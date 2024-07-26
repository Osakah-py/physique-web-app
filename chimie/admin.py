from django.contrib import admin, messages
from django.utils.translation import ngettext
from .models import Categorie, Document

# DOCUMENT MODEL 
@admin.action(description="Rendre visible")
def make_visible(modeladmin, request, queryset):
    updated = queryset.update(visible=True)
    modeladmin.message_user(
            request,
            ngettext(
                "%d document est désormais visible.",
                "Les %d documents sont désormais visibles.",
                updated,
            )
            % updated,
            messages.SUCCESS,
        )

@admin.action(description="Masquer")
def make_hidden(modeladmin, request, queryset):
    updated = queryset.update(visible=False)
    modeladmin.message_user(
            request,
            ngettext(
                "%d document est désormais masqué.",
                "Les %d documents sont désormais masqués.",
                updated,
            )
            % updated,
            messages.SUCCESS,
        )

class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'categorie', 'visible')
    list_filter = ('categorie',)
    actions = [make_visible, make_hidden]

admin.site.register(Document, DocumentAdmin)
admin.site.register(Categorie)
