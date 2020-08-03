from django.db import models
from django.contrib.auth.models import User

class MovieDataBase(models.Model):
    word = models.CharField(max_length=100)
    frequency = models.IntegerField()
    recommendation = models.TextField()

    def __str__(self):
        return self.word
    