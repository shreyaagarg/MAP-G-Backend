from django.db import models
from django.contrib.postgres.fields import ArrayField
from userlogin.models import UserData

# Create your models here.

class emotionPredictorData(models.Model):
    email = models.ForeignKey(UserData, on_delete=models.CASCADE)
    timeChosen = ArrayField(models.DateTimeField())
    answers = ArrayField(models.IntegerField())

    def __str__(self):
        return str(self.uid)