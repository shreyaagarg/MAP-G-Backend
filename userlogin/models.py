from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class UserData(models.Model):
    email = models.EmailField(max_length=100)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    teachingExp = models.IntegerField()
    teachingField = models.IntegerField()
    openID = models.CharField(max_length=100, default='000')
    gender = models.IntegerField(default=1)
    games_played = ArrayField(models.IntegerField())

    def __str__(self):
        return str(self.uid)