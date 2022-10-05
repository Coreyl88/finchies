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

class Feathercolors(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)

    def __str__(self):
        return self.name