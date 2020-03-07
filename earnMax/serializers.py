from rest_framework import serializers
from .models import earnMaxData

class earnMaxDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta():
        model = earnMaxData
        fields = ('uid', 'pile', 'score', 'total')