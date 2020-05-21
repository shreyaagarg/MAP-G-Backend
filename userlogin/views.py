from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer
from .models import UserData
from balloonGame.models import balloonGameData
from earnMax.models import earnMaxData
from emotionPredictor.models import emotionPredictorData
from listeningGame.models import listeningGameData
from django.http import JsonResponse
import ast
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
import json, cv2
from statistics import median
from datetime import datetime
from pathlib import Path
import os
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 

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



def generateReport(request):
    emailToCheck = request.GET.get('emailToCheck')
    all_users = UserData.objects.all()

    if emailToCheck:
        user_present = all_users.filter(email=emailToCheck)

        if not user_present:
            return JsonResponse({'emailToCheck':False})

        '''current_user = all_users.filter(email=emailToCheck).get()
        games_played_by_user = current_user.
'''

        if user_present.exists():
            current_user = all_users.filter(email=emailToCheck).get()
            
            #print('\n\n\n' + str(teaching_exp))
            
            #comparing age
            age_current_user = current_user.age
            userName = current_user.name
            userEmail = current_user.email
            all_users_age = UserData.objects.all().values_list('age', flat=True)
            median_age_all_users = median(all_users_age)

            #comparing teaching experiences
            teaching_exp_current_user = current_user.teachingExp
            all_users_teaching_exp = UserData.objects.all().values_list('teachingExp', flat=True)
            average_teaching_exp = sum(all_users_teaching_exp)/len(all_users_teaching_exp)

            #comparing earnMax scores
            earn_max_current_user = earnMaxData.objects.filter(emailId=emailToCheck).get()
            earn_max_score_current_user = earn_max_current_user.total
            earn_max_score_all_users = earnMaxData.objects.all().values_list('total', flat=True)
            earn_max_score_average = sum(earn_max_score_all_users)/len(earn_max_score_all_users)

            '''
            print('\n\n\n all users score')
            print(earn_max_score_all_users)
            print('\n\n\n current user score')
            print(earn_max_score_current_user)
            print('\n\n\n average user score')
            print(earn_max_score_average)
            '''


            #comparing balloonGame scores
            balloon_game_current_user = balloonGameData.objects.filter(emailId=emailToCheck).get()
            balloon_game_score_current_user = balloon_game_current_user.total
            balloon_game_score_all_users = balloonGameData.objects.all().values_list('total', flat=True)
            balloon_game_score_average = sum(balloon_game_score_all_users)/len(balloon_game_score_all_users)

            '''
            print('\n\n\n all users score')
            print(type(balloon_game_score_all_users))
            print('\n\n\n current user score')
            print(type(balloon_game_score_current_user))
            print('\n\n\n average user score')
            print(type(balloon_game_score_average))
            '''


            '''comparing listeningGame time taken'''
            listeningGame_current_user = listeningGameData.objects.filter(emailId=emailToCheck).get()
            
            #getting startTime in timeObject
            listeningGame_current_user_start_time_uned_str = listeningGame_current_user.audioStart[1]
            '''print('listeningGame_current_user_start_time_uned_str:')
            print(listeningGame_current_user_start_time_uned_str)'''

            listeningGame_current_user_start_time_string = listeningGame_current_user_start_time_uned_str.split(' ')[0]
            '''print('listeningGame_current_user_start_time_string:')
            print(listeningGame_current_user_start_time_string)'''

            listeningGame_current_user_start_time_tiobj = datetime.strptime(listeningGame_current_user_start_time_string, "%H:%M:%S")
            '''print('listeningGame_current_user_start_time_tiobj:')
            print(listeningGame_current_user_start_time_tiobj)'''

            #getting endTime in timeObject
            listeningGame_current_user_end_time_uned_str = listeningGame_current_user.audioEnd[-1]
            '''print('listeningGame_current_user_end_time_uned_str:')
            print(listeningGame_current_user_end_time_uned_str)'''

            listeningGame_current_user_end_time_string = listeningGame_current_user_end_time_uned_str.split(' ')[0]
            '''print('listeningGame_current_user_end_time_string:')
            print(listeningGame_current_user_end_time_string)'''

            listeningGame_current_user_end_time_tiobj = datetime.strptime(listeningGame_current_user_end_time_string, "%H:%M:%S")
            '''print('listeningGame_current_user_end_time_tiobj:')
            print(listeningGame_current_user_end_time_tiobj)'''

            # difference in seconds for current user
            listeningGame_current_user_time_taken = int((listeningGame_current_user_end_time_tiobj - listeningGame_current_user_start_time_tiobj).seconds/60)


            # list of timeObjects of start time of all users
            listeningGame_start_time_all_users_lol = listeningGameData.objects.all().values_list('audioStart', flat=True)
            '''print('listeningGame_start_time_all_users_lol:')
            print(listeningGame_start_time_all_users_lol)'''

            listeningGame_start_time_all_users_uned_str = [x[1] for x in listeningGame_start_time_all_users_lol]
            '''print('listeningGame_start_time_all_users_uned_str:')
            print(listeningGame_start_time_all_users_uned_str)'''

            listeningGame_start_time_all_users_string = [x.split(' ')[0] for x  in listeningGame_start_time_all_users_uned_str]
            '''print('listeningGame_start_time_all_users_string:')
            print(listeningGame_start_time_all_users_string)'''

            listeningGame_start_time_all_users_tiobj = [ datetime.strptime(x, "%H:%M:%S") for x in listeningGame_start_time_all_users_string]
            '''print('listeningGame_start_time_all_users_tiobj:')
            print(listeningGame_start_time_all_users_tiobj)'''

            # list of timeObjects of start time of all users
            listeningGame_end_time_all_users_lol = listeningGameData.objects.all().values_list('audioEnd', flat=True)
            '''print('listeningGame_end_time_all_users_lol:')
            print(listeningGame_end_time_all_users_lol)'''

            listeningGame_end_time_all_users_uned_str = [x[-1] for x in listeningGame_end_time_all_users_lol]
            '''print('listeningGame_end_time_all_users_uned_str:')
            print(listeningGame_end_time_all_users_uned_str)'''

            listeningGame_end_time_all_users_string = [x.split(' ')[0] for x  in listeningGame_end_time_all_users_uned_str]
            '''print('listeningGame_end_time_all_users_string:')
            print(listeningGame_end_time_all_users_string)'''

            listeningGame_end_time_all_users_tiobj = [ datetime.strptime(x, "%H:%M:%S") for x in listeningGame_end_time_all_users_string]
            '''print('listeningGame_end_time_all_users_tiobj:')
            print(listeningGame_end_time_all_users_tiobj)'''

            # time taken in seconds for all users
            time_taken_all_users = [int((y-x).seconds/60) for x,y in zip(listeningGame_start_time_all_users_tiobj, listeningGame_end_time_all_users_tiobj)]
            '''print('time_taken_all_users:')
            print(time_taken_all_users)'''

            av_time_taken_all_users = int(sum(time_taken_all_users)/len(time_taken_all_users))


            '''
            print('\n\n\n all user time taken')
            print(time_taken_all_users)
            print('\n\n\n average user time taken')
            print(av_time_taken_all_users)
            '''


            '''comparing listeningGame # of pauses'''
            listeningGame_current_user = listeningGameData.objects.filter(emailId=emailToCheck).get()
            listeningGame_pauses_current_user = len(listeningGame_current_user.audioPause)
            listeningGame_pauses_all_users_lol = listeningGameData.objects.all().values_list('audioPause', flat=True)
            listeningGame_pauses_all_users_list = [ len(x) for x in listeningGame_pauses_all_users_lol]
            listeningGame_pauses_average = int(sum(listeningGame_pauses_all_users_list)/len(listeningGame_pauses_all_users_list))

            '''
            print('\n\n\n all users pause')
            print(listeningGame_pauses_all_users_list)
            print('\n\n\n current user pause')
            print(listeningGame_pauses_current_user)
            print('\n\n\n average user pause')
            print(listeningGame_pauses_average)
            '''
            imgPath = "report-template-small.jpg"
            image = cv2.imread(imgPath)
            
            # cv2.namedWindow('one',cv2.WINDOW_NORMAL)
            # cv2.resizeWindow('one', 600, 600)
            # cv2.imshow('one',image)
            # cv2.waitKey(0)

            temp_img = cv2.putText(image,str(userName), (50,488), cv2.FONT_HERSHEY_DUPLEX, 1.8, (39, 39, 217), 6)

            #age
            temp_img1 = cv2.putText(temp_img, str(age_current_user), (365,739), cv2.FONT_HERSHEY_DUPLEX, 1.8, (39, 39, 217), 6)
            temp_img2 = cv2.putText(temp_img1, str(median_age_all_users), (1406,739), cv2.FONT_HERSHEY_DUPLEX, 1.8 , (39, 39, 217),6)

            #teaching exp
            temp_img3 = cv2.putText(temp_img2, str(teaching_exp_current_user), (513, 1048), cv2.FONT_HERSHEY_DUPLEX, 1.8, (39, 39, 217),6)
            temp_img4 = cv2.putText(temp_img3, str(average_teaching_exp), (1571, 1048), cv2.FONT_HERSHEY_DUPLEX, 1.8, (39, 39, 217), 6)

            #earnmax score
            temp_img5 = cv2.putText(temp_img4, str(earn_max_score_current_user), (308,1346),cv2.FONT_HERSHEY_DUPLEX,1.8,(39, 39, 217),6)
            temp_img6 = cv2.putText(temp_img5, str(earn_max_score_average), (1364, 1346),cv2.FONT_HERSHEY_DUPLEX,1.8,(39, 39, 217),6)

            #balloon score
            temp_img7 = cv2.putText(temp_img6, str(balloon_game_score_current_user), (308, 1666),cv2.FONT_HERSHEY_DUPLEX,1.8,(39, 39, 217),6)
            temp_img8 = cv2.putText(temp_img7, str(balloon_game_score_average) ,(1364, 1666),cv2.FONT_HERSHEY_DUPLEX,1.8,(39, 39, 217),6)

            #listen 1
            temp_img9 = cv2.putText(temp_img8, str(listeningGame_current_user_time_taken), (461, 1987),cv2.FONT_HERSHEY_DUPLEX,1.8,(39, 39, 217),6)
            temp_img10 = cv2.putText(temp_img9, str(av_time_taken_all_users), (1478, 1987),cv2.FONT_HERSHEY_DUPLEX,1.8,(39, 39, 217),6)

            #listen 2
            temp_img11 = cv2.putText(temp_img10, str(listeningGame_pauses_current_user), (719, 2305),cv2.FONT_HERSHEY_DUPLEX,1.8,(39, 39, 217),6)
            temp_img12 = cv2.putText(temp_img11, str(listeningGame_pauses_average), (1744, 2305),cv2.FONT_HERSHEY_DUPLEX,1.8,(39, 39, 217),6)

            imgOpPath = 'C:/Users/Paritosh_Malhotra/Desktop/MAPG_backend_github/'
            imgName = 'report_'+str(userName)+'.jpg'

            # print('imgName')
            # print(imgName)
            # print(ImgOpPath+imgName)

            # cv2.namedWindow('two',cv2.WINDOW_NORMAL)
            # cv2.resizeWindow('two', 600, 600)
            # cv2.imshow('two',temp_img12)
            # cv2.waitKey(0)

            cv2.imwrite(imgName, temp_img12)
            

            fromaddr = "mapg.project@gmail.com"
            toaddr = userEmail
            
            # instance of MIMEMultipart 
            msg = MIMEMultipart() 
            # storing the senders email address   
            msg['From'] = fromaddr 
            # storing the receivers email address  
            msg['To'] = toaddr 
            # storing the subject  
            msg['Subject'] = "MAP-G Psychometric Report"
            
            # string to store the body of the mail 
            body = "Hello "+str(userName)+' , thank you for taking part in the MAP-G project. Please find your report attached with this email. \n\nRegards, \nMAP-G Team'
            
            # attach the body with the msg instance 
            msg.attach(MIMEText(body, 'plain')) 
            
            # open the file to be sent  
            filename = imgName
            attachment = open(str(imgName), "rb") 
            
            # instance of MIMEBase and named as p 
            p = MIMEBase('application', 'octet-stream') 
            
            # To change the payload into encoded form 
            p.set_payload((attachment).read()) 
            
            # encode into base64 
            encoders.encode_base64(p) 
            
            p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
            
            # attach the instance 'p' to instance 'msg' 
            msg.attach(p) 
            
            # creates SMTP session 
            s = smtplib.SMTP('smtp.gmail.com', 587) 
            
            # start TLS for security 
            s.starttls() 
            
            # Authentication 
            s.login(fromaddr, "adminmapg123") 
            
            # Converts the Multipart msg into a string 
            text = msg.as_string() 
            
            # sending the mail 
            s.sendmail(fromaddr, toaddr, text) 
            
            # terminating the session 
            s.quit() 


            return JsonResponse({'emailToCheck':True})



        else:
            return JsonResponse({'emailToCheck':False})

    else:
        return JsonResponse({'data':'not_sent'})
    