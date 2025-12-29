# mbolafy/accueil/models.py

from django.db import models

class Hero(models.Model):
    nom_complet = models.CharField(
        max_length=150,
        verbose_name="Nom complet"
    )
    prenom = models.CharField(
        max_length=100,
        verbose_name="Prénom / Pseudo"
    )
    metier = models.CharField(
        max_length=150,
        verbose_name="Métier"
    )
    description = models.TextField(
        blank=True,
        verbose_name="Description"
    )
    image = models.ImageField(
        upload_to='hero/',
        verbose_name="Image de profil"
    )
    icon = models.CharField(
        max_length=50,
        default="fa-laptop-code",
        verbose_name="Icône FontAwesome"
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="Actif"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Accueil - Profil"
        verbose_name_plural = "Accueil - Profils"

    def __str__(self):
        return self.nom_complet
