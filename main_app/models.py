from django.db import models
from django.contrib.auth.models import User

class Finch(models.Model):
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=300)
    bio = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Sighting(models.Model):
    name = models.CharField(max_length=200, default='unknown')
    location = models.CharField(max_length=200)
    finch = models.ForeignKey(Finch, on_delete=models.CASCADE, related_name="sightings")

    def __str__(self):
        return self.name

class Feather(models.Model):
    color = models.CharField(max_length=100)
    finch = models.ManyToManyField(Finch)

    def __str__(self):
        return self.color