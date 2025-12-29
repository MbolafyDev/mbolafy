from django.contrib import admin
from .models import Hero


@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    # Colonnes visibles dans la liste
    list_display = (
        'nom_complet',
        'prenom',
        'metier',
        'is_active',
        'created_at',
    )

    # Filtres à droite
    list_filter = (
        'is_active',
        'created_at',
    )

    # Champ de recherche
    search_fields = (
        'nom_complet',
        'prenom',
        'metier',
    )

    # Édition rapide depuis la liste
    list_editable = (
        'is_active',
    )

    # Ordre d’affichage
    ordering = ('-created_at',)

    # Organisation du formulaire
    fieldsets = (
        ("Informations personnelles", {
            'fields': ('nom_complet', 'prenom', 'image')
        }),
        ("Profession", {
            'fields': ('metier', 'icon')
        }),
        ("Présentation", {
            'fields': ('description',)
        }),
        ("Paramètres", {
            'fields': ('is_active',)
        }),
    )

    # Lecture seule
    readonly_fields = ('created_at',)
