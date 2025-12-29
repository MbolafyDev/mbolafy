# mbolafy/parcour/models.py

from django.db import models

class Experience(models.Model):
    titre = models.CharField(
        max_length=150,
        verbose_name="Poste / Titre"
    )
    entreprise = models.CharField(
        max_length=150,
        verbose_name="Entreprise",
        blank=True,
        null=True
    )
    date_debut = models.CharField(
        max_length=50,
        verbose_name="Date de début"
    )
    date_fin = models.CharField(
        max_length=50,
        verbose_name="Date de fin"
    )
    description = models.TextField(
        verbose_name="Description"
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="Actif"
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        verbose_name = "Expérience"
        verbose_name_plural = "Expériences"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.titre} - {self.entreprise}"
