from django.shortcuts import render
from rest_framework import viewsets
from .serializers import listeningGameDataSerializer
from .models import listeningGameData

# Create your views here.

class ListeningGameViewSet(viewsets.ModelViewSet):
    queryset = listeningGameData.objects.all().order_by('uid')
    serializer_class = listeningGameDataSerializer

