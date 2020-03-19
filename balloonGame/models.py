from django.db import models
from django.contrib.postgres.fields import ArrayField
from userlogin.models import UserData


# Create your models here.

class balloonGameData(models.Model):
    email = models.ForeignKey(UserData, on_delete=models.CASCADE)
    color = ArrayField(models.IntegerField())
    clicks = ArrayField(models.IntegerField())
    amount = ArrayField(models.IntegerField())
    total = models.IntegerField()


    def __str__(self):
        return str(self.email)

