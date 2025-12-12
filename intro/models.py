from django.db import models

class About(models.Model):
    content = models.TextField(help_text="Texte décrivant à propos de moi")

    def __str__(self):
        # Retourne les 50 premiers caractères pour une lecture rapide
        return self.content[:50] + ("..." if len(self.content) > 50 else "")
