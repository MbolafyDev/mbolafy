# projet/models.py

from django.db import models

class Projet(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    images = models.JSONField(blank=True, null=True, help_text="Liste d'URL ou chemins des images du projet")
    code_url = models.URLField(blank=True, null=True, help_text="Lien vers le code source")
    demo_url = models.URLField(blank=True, null=True, help_text="Lien vers la démo en ligne")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
