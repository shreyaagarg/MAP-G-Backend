from rest_framework import serializers
from .models import earnMaxData

class earnMaxDataSerializer(serializers.ModelSerializer):
    class Meta():
        model = earnMaxData
        fields = ('uid', 'pile', 'scores', 'total')