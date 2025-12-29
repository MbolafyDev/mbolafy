# mbolafy/parcour/models.py

from django.db import models

class Competence(models.Model):
    icone = models.CharField(
        max_length=50,
        help_text="Classe FontAwesome de l'icône (ex: fab fa-python)"
    )
    titre = models.CharField(
        max_length=100,
        verbose_name="Titre de la compétence"
    )
    description = models.CharField(
        max_length=255,
        verbose_name="Description courte"
    )
    niveau = models.PositiveIntegerField(
        verbose_name="Niveau (%)",
        help_text="Valeur entre 0 et 100 pour la barre de progression"
    )
    ordre = models.PositiveIntegerField(
        default=0,
        help_text="Ordre d'affichage dans le template"
    )

    class Meta:
        verbose_name = "Compétence"
        verbose_name_plural = "Compétences"
        ordering = ['ordre']

    def __str__(self):
        return f"{self.titre} ({self.niveau}%)"
