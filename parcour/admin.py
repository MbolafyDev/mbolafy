# mbolafy/parcour/models.py

from django.contrib import admin
from .models import Parcours


@admin.register(Parcours)
class ParcoursAdmin(admin.ModelAdmin):
    list_display = (
        'titre',
        'annee_debut',
        'annee_fin',
        'ordre',
        'is_active',
        'created_at'
    )

    list_editable = (
        'ordre',
        'is_active',
    )

    list_filter = (
        'is_active',
        'annee_debut',
    )

    search_fields = (
        'titre',
        'description',
    )

    ordering = (
        'ordre',
        '-annee_debut',
    )

    fieldsets = (
        ("Informations principales", {
            'fields': (
                'titre',
                'description',
            )
        }),
        ("Période", {
            'fields': (
                'annee_debut',
                'annee_fin',
            )
        }),
        ("Affichage", {
            'fields': (
                'ordre',
                'is_active',
            )
        }),
        ("Métadonnées", {
            'fields': (
                'created_at',
                'updated_at',
            )
        }),
    )

    readonly_fields = (
        'created_at',
        'updated_at',
    )
