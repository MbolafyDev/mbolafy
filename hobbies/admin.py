# hobbies/admin.py

from django.contrib import admin
from .models import Hobby

@admin.register(Hobby)
class HobbyAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon')        # Colonnes affichées dans la liste
    search_fields = ('name', 'icon')       # Barre de recherche par nom ou icône
    list_filter = ('icon',)                # Filtrage par icône
    ordering = ('name',)                   # Ordre par défaut alphabétique
