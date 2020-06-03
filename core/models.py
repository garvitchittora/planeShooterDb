from django.db import models

# Create your models here.

class leaderboard(models.Model):
    name = models.CharField(max_length = 1000)
    score = models.IntegerField()
    def __str__(self): 
        return self.name
