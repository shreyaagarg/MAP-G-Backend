from django.shortcuts import render
from rest_framework import viewsets
from .serializers import earnMaxDataSerializer
from .models import earnMaxData

# Create your views here.

class EarnMaxViewSet(viewsets.ModelViewSet):
    queryset = earnMaxData.objects.all().order_by('emailId')
    serializer_class = earnMaxDataSerializer

