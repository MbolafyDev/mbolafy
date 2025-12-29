# mbolafy/parcour/models.py

from django.contrib import admin
from .models import ContactInfo

@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('location', 'phone', 'email', 'is_active', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('location', 'phone', 'email')
