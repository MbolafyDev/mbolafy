# mbolafy/parcour/models.py

from django.contrib import admin
from .models import Experience

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = (
        'titre',
        'entreprise',
        'date_debut',
        'date_fin',
        'is_active'
    )
    list_filter = ('is_active',)
    search_fields = ('titre', 'entreprise')
    list_editable = ('is_active',)
