# mbolafy/projet/models.py
from django.db import models

class Projet(models.Model):
    titre = models.CharField(max_length=200, verbose_name="Titre du projet")
    description = models.TextField(verbose_name="Description")
    image = models.ImageField(
        upload_to='projets/',  # les images seront stockées dans MEDIA_ROOT/projets/
        verbose_name="Image du projet"
    )
    lien = models.URLField(max_length=500, blank=True, null=True, verbose_name="Lien du projet")
    is_active = models.BooleanField(default=True, verbose_name="Actif ?")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Dernière mise à jour")

    class Meta:
        verbose_name = "Projet"
        verbose_name_plural = "Projets"
        ordering = ['-created_at']

    def __str__(self):
        return self.titre
