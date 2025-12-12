# contact/admin.py

from django.contrib import admin
from .models import ContactInfo

@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone', 'website', 'location')  # Colonnes affichées dans la liste
    search_fields = ('email', 'phone', 'location')            # Barre de recherche
    list_filter = ('location',)                                # Filtrage par localisation
    ordering = ('email',)                                      # Ordre par défaut
