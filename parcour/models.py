# mbolafy/parcour/models.py

from django.db import models


class Parcours(models.Model):
    titre = models.CharField(
        max_length=150,
        verbose_name="Titre du parcours"
    )

    annee_debut = models.PositiveIntegerField(
        verbose_name="Année de début"
    )

    annee_fin = models.PositiveIntegerField(
        verbose_name="Année de fin"
    )

    description = models.TextField(
        verbose_name="Description",
        blank=True
    )

    ordre = models.PositiveIntegerField(
        default=0,
        help_text="Ordre d'affichage sur le site"
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name="Afficher sur le site"
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Date de création"
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Dernière modification"
    )

    class Meta:
        verbose_name = "Parcours"
        verbose_name_plural = "Parcours"
        ordering = ['ordre', '-annee_debut']

    def __str__(self):
        return f"{self.titre} ({self.annee_debut} - {self.annee_fin})"
