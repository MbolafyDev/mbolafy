from django.contrib import admin
from .models import Projet

@admin.register(Projet)
class ProjetAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "code_url", "demo_url")
    list_filter = ("created_at",)
    search_fields = ("title", "description")
    ordering = ("-created_at",)
    readonly_fields = ("created_at",)
