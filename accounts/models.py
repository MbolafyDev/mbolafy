# accounts/models.py

from django.db import models

class Profile(models.Model):
    full_name = models.CharField(max_length=200)
    job_title = models.CharField(max_length=200)
    bio = models.TextField(blank=True)

    profile_picture = models.ImageField(upload_to='profile/', blank=True, null=True)
    cover_picture = models.ImageField(upload_to='cover/', blank=True, null=True)

    followers = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.full_name
