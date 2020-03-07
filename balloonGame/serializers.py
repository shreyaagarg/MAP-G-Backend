from rest_framework import serializers
from .models import balloonGameData

class balloonGameDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta():
        model = balloonGameData
        fields = ('uid', 'color', 'clicks', 'clicks', 'amount', 'total')