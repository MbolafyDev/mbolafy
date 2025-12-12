from django.contrib import admin
from .models import Projet, ProjectImage

# Inline pour gérer les images directement dans l'admin du projet
class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1  # nombre de champs supplémentaires pour ajouter une nouvelle image
    readonly_fields = ("uploaded_at",)

@admin.register(Projet)
class ProjetAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "code_url", "demo_url")
    list_filter = ("created_at",)
    search_fields = ("title", "description")
    ordering = ("-created_at",)
    readonly_fields = ("created_at",)
    inlines = [ProjectImageInline]  # ajoute l'inline ici

# Optionnel : tu peux aussi enregistrer ProjectImage séparément si tu veux
# admin.site.register(ProjectImage)
