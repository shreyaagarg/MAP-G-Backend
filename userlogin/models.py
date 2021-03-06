from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class UserData(models.Model):
    email = models.EmailField(primary_key=True, max_length=100)
    name = models.CharField(max_length=50, default='')
    age = models.IntegerField(default=0)
    teachingExp = models.IntegerField(default=0)
    teachingField = models.IntegerField(default=0)
    openID = models.CharField(max_length=100, default='000')
    gender = models.IntegerField(default=1)
    games_played = ArrayField(models.BooleanField(), default = list)

    def __str__(self):
        return str(self.email_id)