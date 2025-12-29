# mbolafy/parcour/models.py

# contact/models.py
from django.db import models

class ContactInfo(models.Model):
    location = models.CharField(max_length=255, verbose_name="Adresse / Localisation")
    phone = models.CharField(max_length=20, verbose_name="Téléphone")
    email = models.EmailField(verbose_name="Email")
    is_active = models.BooleanField(default=True, verbose_name="Actif")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.location} - {self.phone}"
