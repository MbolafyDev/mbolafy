from django.db import models

class Quality(models.Model):
    icon = models.CharField(max_length=50, default="fa-check-circle")
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text

class Language(models.Model):
    LEVEL_CHOICES = [
        ('débutant', 'Débutant'),
        ('intermédiaire', 'Intermédiaire'),
        ('avancé', 'Avancé'),
        ('expert', 'Expert'),
    ]

    name = models.CharField(max_length=100)
    level = models.CharField(
        max_length=20,
        choices=LEVEL_CHOICES,
        default='intermédiaire',
        help_text="Niveau de compétence"
    )

    def __str__(self):
        return f"{self.name} - {self.get_level_display()}"
