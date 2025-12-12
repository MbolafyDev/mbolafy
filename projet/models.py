# projet/models.py

from django.db import models

class Projet(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    code_url = models.URLField(blank=True, null=True, help_text="Lien vers le code source")
    demo_url = models.URLField(blank=True, null=True, help_text="Lien vers la démo en ligne")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ProjectImage(models.Model):
    projet = models.ForeignKey(Projet, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="projets/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.projet.title} - Image {self.id}"
