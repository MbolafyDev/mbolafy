# mbolafy/parcour/models.py

from django.contrib import admin
from .models import Projet

@admin.register(Projet)
class ProjetAdmin(admin.ModelAdmin):
    list_display = ('titre', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('titre', 'description')
    readonly_fields = ('created_at', 'updated_at')
