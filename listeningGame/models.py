from django.db import models
from django.contrib.postgres.fields import ArrayField
from userlogin.models import UserData

# Create your models here.

class listeningGameData(models.Model):
    uid = models.ForeignKey('userlogin.UserData', on_delete=models.CASCADE)
    startTime = models.DateTimeField()
    ans1 = models.DateTimeField()
    ans2 = models.DateTimeField()
    ans3 = models.DateTimeField()
    pauseTimeStart = ArrayField(models.DateTimeField())
    pauseTimeEnd = ArrayField(models.DateTimeField())
    adjustTimings = ArrayField(models.DateTimeField())


    def __str__(self):
        return self.uid
    