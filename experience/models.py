from django.db import models

class Experience(models.Model):
    TYPE_CHOICES = [
        ('parcours', 'Parcours'),
        ('experience', 'Expérience professionnelle'),
    ]

    year = models.CharField(max_length=20)
    icon = models.CharField(max_length=50, default="fa-briefcase")
    title = models.CharField(max_length=200)
    description = models.TextField()
    color = models.CharField(max_length=20, default="#1877f2")  # Couleur du badge
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='experience')

    def __str__(self):
        return f"{self.year} - {self.title}"

