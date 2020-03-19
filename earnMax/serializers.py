from rest_framework import serializers
from .models import earnMaxData

class earnMaxDataSerializer(serializers.ModelSerializer):
    class Meta():
        model = earnMaxData
        fields = ('emailId', 'pile', 'scores', 'total')