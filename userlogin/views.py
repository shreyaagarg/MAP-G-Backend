from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer
from .models import UserData

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = UserData.objects.all().order_by('uid')
    serializer_class = UserSerializer