# about/admin.py

from django.contrib import admin
from .models import IntroItem

@admin.register(IntroItem)
class IntroItemAdmin(admin.ModelAdmin):
    list_display = ('text', 'icon')  # Colonnes affichées dans la liste
    search_fields = ('text', 'icon')  # Barre de recherche
    list_filter = ('icon',)           # Filtrage par icône si besoin
    ordering = ('text',)              # Ordre par défaut
