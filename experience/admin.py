# experience/admin.py

from django.contrib import admin
from .models import Experience

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('year', 'title', 'type', 'icon', 'color')  # Colonnes affichées
    list_filter = ('type', 'year')                              # Filtrage par type et année
    search_fields = ('title', 'description')                    # Barre de recherche
    ordering = ('-year',)                                       # Ordre décroissant par année
    fieldsets = (
        ('Informations principales', {
            'fields': ('year', 'type', 'title', 'description')
        }),
        ('Affichage', {
            'fields': ('icon', 'color')
        }),
    )
