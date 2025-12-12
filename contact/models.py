from django.db import models

class ContactInfo(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    website = models.URLField(blank=True)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.email
