from django.db import models
from django.contrib.postgres.fields import ArrayField
from userlogin.models import UserData


# Create your models here.

class balloonGameData(models.Model):
    emailId = models.EmailField(max_length=100, primary_key=True, default='')
    color = ArrayField(models.IntegerField())
    clicksBursted = ArrayField(models.IntegerField(), default=list)
    clicksCollected = ArrayField(models.IntegerField(), default=list)
    amountCollected = ArrayField(models.IntegerField(), default=list)
    total = models.IntegerField()


    def __str__(self):
        return str(self.emailId)

