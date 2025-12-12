# competence/models.py

from django.db import models

class Competence(models.Model):
    name = models.CharField(max_length=100)
    level = models.PositiveIntegerField(help_text="Pourcentage (0-100)")
    color_class = models.CharField(max_length=20, default="bg-primary", help_text="Classe bootstrap pour la couleur de la barre de progression")

    def __str__(self):
        return f"{self.name} ({self.level}%)"
