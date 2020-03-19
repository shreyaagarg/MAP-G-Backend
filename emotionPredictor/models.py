from django.db import models
from django.contrib.postgres.fields import ArrayField
from userlogin.models import UserData

# Create your models here.

class emotionPredictorData(models.Model):
    emailId = models.EmailField(max_length=100, primary_key=True, default='')
    timeChosen = ArrayField(models.DateTimeField())
    answers = ArrayField(models.IntegerField())

    def __str__(self):
        return str(self.emailId)