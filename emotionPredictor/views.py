from django.shortcuts import render
from rest_framework import viewsets
from .serializers import emotionPredictorDataSerializer
from .models import emotionPredictorData

# Create your views here.

class EmotionPredictorViewSet(viewsets.ModelViewSet):
    queryset = emotionPredictorData.objects.all().order_by('email')
    serializer_class = emotionPredictorDataSerializer

