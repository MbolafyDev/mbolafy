from django.contrib import admin
from .models import About

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('short_content',)

    def short_content(self, obj):
        # Affiche un résumé du contenu
        return obj.content[:50] + ("..." if len(obj.content) > 50 else "")
    short_content.short_description = "À propos"
