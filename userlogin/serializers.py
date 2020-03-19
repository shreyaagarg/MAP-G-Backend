from rest_framework import serializers
from .models import UserData

class UserSerializer(serializers.ModelSerializer):
    class Meta():
        model = UserData
        fields = ('email', 'name', 'age', 'teachingExp', 'teachingField', 'openID', 'gender', 'games_played')