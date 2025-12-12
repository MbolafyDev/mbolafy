from django.contrib import admin
from .models import Competence

@admin.register(Competence)
class CompetenceAdmin(admin.ModelAdmin):
    list_display = ("name", "level", "color_class")
    list_filter = ("color_class",)
    search_fields = ("name",)
    ordering = ("-level",)
