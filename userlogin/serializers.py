from rest_framework import serializers
from .models import UserData

class UserSerializer(serializers.ModelSerializer):
    class Meta():
        model = UserData
        fields = ('uid', 'email', 'name', 'age', 'teachingExp', 'teachingField')