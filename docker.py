import os
import speech_recognition as sr
import pyttsx3

from athtasktry import ip

def dockerconf():
    print("-----------DOCKER----------")
    print("1. Docker daemon start/stop/status")
    print("2. Show docker process")
    print("3. Show docker images")
    print("4. Download imag on docker.")
    print("5. Launch O.S on docker hub")
    print("7. Stop docker container")
    print("8. Delete docker image")
   
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            pyttsx3.speak("start speaking...and tell me next.")
            print("I am capturing Your requirement..")
            audio = r.listen(source)
            print("Your requirement is captured.")
        select = r.recognize_google(audio)
        if ("start" in select):
            os.system('ssh root@{} systemctl start docker'.format(ip))
        elif ("stop" in select):
                os.system('ssh root@{} systemctl stop docker'.format(ip))
        elif ("status" in select):
                os.system('ssh root@{} sytemctl status docker'.format(ip))
        elif ("recent" in select):
                os.system('ssh root@{} docker ps'.format(ip))
        elif ("all" in select):
                os.system('ssh root@{} docker ps -a'.format(ip))
        elif ("images" in select):
            os.system('ssh root@{} docker images'.format(ip))
        elif ("download" in select):
            im = input('image name - ')
            os.system('ssh root@{0} docker pull {1}'.format(ip,im))
        elif ("launch" in select):
            im = input('image name - ')
            os.system('ssh root@{0} docker run -it {1} &'.format(ip,im))
        elif ("container" in select):
            im = input('image name - ')
            os.system('ssh root@{0} docker stop {1}'.format(ip,im))
        elif ("delete" in select):
            im = input('image name - ')
            os.system('ssh root@{0} docker rmi {1}'.format(ip,im))
        elif ("thanks" in select):
            pyttsx3.speak("okay thank you for visiting")
            return
        else:
            print('Error')
