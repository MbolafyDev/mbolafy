from django.db import models

# Create your models here.
class Quality(models.Model):
    icon = models.CharField(max_length=50, default="fa-check-circle")
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text

class Language(models.Model):
    name = models.CharField(max_length=100)
    level = models.PositiveIntegerField(help_text="Pourcentage (0-100)")

    def __str__(self):
        return f"{self.name} - {self.level}%"
