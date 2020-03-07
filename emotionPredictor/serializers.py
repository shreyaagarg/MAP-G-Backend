from rest_framework import serializers
from .models import emotionPredictorData

class emotionPredictorDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta():
        model = emotionPredictorData
        fields = ('uid', 'timeChosen', 'answers')