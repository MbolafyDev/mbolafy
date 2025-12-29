# mbolafy/parcour/models.py

from django.contrib import admin
from .models import Competence

@admin.register(Competence)
class CompetenceAdmin(admin.ModelAdmin):
    list_display = ('titre', 'niveau', 'ordre')
    list_editable = ('niveau', 'ordre')
    search_fields = ('titre', 'description')
    list_filter = ('niveau',)
