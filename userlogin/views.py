from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer
from .models import UserData
from django.http import JsonResponse
import ast
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
import json

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
            return JsonResponse({'emailToCheck':False})

        current_user = all_users.filter(email=emailToCheck).get()
        games_played_by_user = current_user.games_played


        if user_present.exists():
            return JsonResponse({'emailToCheck':True,
                                    'games_played': games_played_by_user})
        else:
            return JsonResponse({'emailToCheck':False})

    else:
        return JsonResponse({'data':'not_sent'})



@require_POST
@csrf_exempt
def updateGamesPlayed(request):

    if request.method== 'POST':
        #set encoding of string and load the response into json
        body_unicode = request.body.decode('utf-8')
        json_data = json.loads(body_unicode)

        user_email = json_data['email']
        games_played_string = json_data['games_played']

        games_played_string = games_played_string.replace('true', 'True')
        games_played_string = games_played_string.replace('false', 'False')

        # print(user_email)
        # print(games_played_string)
        user_games_played = list(eval(games_played_string))
        all_users = UserData.objects.all()
        
        if user_email and user_games_played:
            user_present = all_users.filter(email=user_email)
            if not user_present:
                return JsonResponse({'Email':'invalid'})
                
            current_user = all_users.filter(email=user_email).get()
            current_user.games_played = user_games_played
            current_user.save()
            return JsonResponse({'update':'successful'})
