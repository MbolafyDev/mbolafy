# skills/admin.py

from django.contrib import admin
from .models import Quality, Language

@admin.register(Quality)
class QualityAdmin(admin.ModelAdmin):
    list_display = ('text', 'icon')         # Colonnes affichées dans la liste
    search_fields = ('text',)               # Barre de recherche par texte
    list_filter = ('icon',)                 # Filtrage par icône
    ordering = ('text',)                    # Tri alphabétique

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name', 'level')       # Colonnes affichées
    search_fields = ('name',)              # Recherche par nom
    list_filter = ('level',)               # Filtrage par niveau
    ordering = ('-level',)                 # Tri décroissant par niveau
