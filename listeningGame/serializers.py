from rest_framework import serializers
from .models import listeningGameData

class listeningGameDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta():
        model = listeningGameData
        fields = ('uid', 'startTime', 'ans1', 'ans2', 'ans3', 'pauseTimeStart', 'pauseTimeEnd', 'adjustTimings')