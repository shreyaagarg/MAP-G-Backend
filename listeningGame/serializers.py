from rest_framework import serializers
from .models import listeningGameData

class listeningGameDataSerializer(serializers.ModelSerializer):
    class Meta():
        model = listeningGameData
        fields = ('emailId', 'audioStart', 'audioPause', 'audioEnd', 'audioAdjust', 'answers')