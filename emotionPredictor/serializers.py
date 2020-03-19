from rest_framework import serializers
from .models import emotionPredictorData

class emotionPredictorDataSerializer(serializers.ModelSerializer):
    class Meta():
        model = emotionPredictorData
        fields = ('uid', 'timeChosen', 'answers')