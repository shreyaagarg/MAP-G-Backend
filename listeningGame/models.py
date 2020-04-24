from django.db import models
from django.contrib.postgres.fields import ArrayField
from userlogin.models import UserData

# Create your models here.

class listeningGameData(models.Model):
    emailId = models.EmailField(max_length=100, primary_key=True, default='')
    
    # ans1 = models.DateTimeField()
    # ans2 = models.DateTimeField()
    # ans3 = models.DateTimeField()
    audioStart =  ArrayField(models.CharField(max_length=100, default='000'), default = list)
    audioPause =  ArrayField(models.CharField(max_length=100, default='000'), default = list)
    audioEnd =    ArrayField(models.CharField(max_length=100, default='000'), default = list)
    audioAdjust = ArrayField(models.CharField(max_length=100, default='000'), default = list)

    answers = ArrayField(ArrayField(models.CharField(max_length=100, default='000'), default=list), default = list)



    def __str__(self):
        return str(self.emailId)
    