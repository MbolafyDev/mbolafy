# photos/admin.py

from django.contrib import admin
from .models import Photo

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'uploaded_at')   # Colonnes affichées dans la liste
    list_filter = ('uploaded_at',)                  # Filtrage par date d'upload
    ordering = ('-uploaded_at',)                    # Affiche les plus récentes en premier
    search_fields = ('id',)                         # Recherche par ID
