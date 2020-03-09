from django.db import models

# Create your models here.

class UserData(models.Model):
    uid = models.BigIntegerField(primary_key=True)
    email = models.EmailField(max_length=100)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    teachingExp = models.IntegerField()
    teachingField = models.IntegerField()

    def __str__(self):
        return str(self.uid)