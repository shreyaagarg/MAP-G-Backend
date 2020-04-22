from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer
from .models import UserData
from django.http import JsonResponse

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = UserData.objects.all().order_by('email')
    serializer_class = UserSerializer


def userExist(request):
    emailToCheck = request.GET.get('emailToCheck')
    all_users = UserData.objects.all()

    if emailToCheck:


        user_present = all_users.filter(email=emailToCheck)

        if not user_present:
            return JsonResponse({emailToCheck:"false"})

        current_user = all_users.filter(email=emailToCheck).get()
        games_played_by_user = current_user.games_played


        if user_present.exists():
            return JsonResponse({emailToCheck:"true",
                                    'games_played': games_played_by_user})
        else:
            return JsonResponse({emailToCheck:"false"})

    else:
        return JsonResponse({'data':'not_sent'})
