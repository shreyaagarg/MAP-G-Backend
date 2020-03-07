from django.db import models
from django.contrib.postgres.fields import ArrayField
from userlogin.models import UserData

# Create your models here.

class earnMaxData(models.Model):
    uid = models.ForeignKey('userlogin.UserData', on_delete=models.CASCADE)
    pile = ArrayField(models.IntegerField())
    scores = ArrayField(models.IntegerField())
    total = models.IntegerField()