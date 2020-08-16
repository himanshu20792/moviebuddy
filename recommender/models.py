from django.db import models

class MovieDataBase(models.Model):
    word = models.CharField(max_length=100)
    recommendation = models.TextField()

    def __str__(self):
        return self.word

class ContentRec(models.Model):
    title = models.TextField()
    genres = models.TextField()
    keywords = models.TextField()
    popularity = models.TextField()
    average_vote = models.TextField()
    num_votes = models.TextField()

    def __str__(self):
        return self.title
    