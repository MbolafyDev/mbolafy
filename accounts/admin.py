# accounts/admin.py

from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'job_title', 'followers')  # Colonnes affichées
    search_fields = ('full_name', 'job_title')  # Barre de recherche
    list_filter = ('job_title',)  # Filtre sur le côté
    readonly_fields = ('followers',)  # Champ en lecture seule
    fieldsets = (
        ('Informations personnelles', {
            'fields': ('full_name', 'job_title', 'bio')
        }),
        ('Photos', {
            'fields': ('profile_picture', 'cover_picture')
        }),
        ('Statistiques', {
            'fields': ('followers',)
        }),
    )
