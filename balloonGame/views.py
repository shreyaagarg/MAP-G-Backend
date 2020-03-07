from django.shortcuts import render
from rest_framework import viewsets
from .serializers import balloonGameDataSerializer
from .models import balloonGameData

# Create your views here.

class BalloonViewSet(viewsets.ModelViewSet):
    queryset = balloonGameData.objects.all().order_by('uid')
    serializer_class = balloonGameDataSerializer

