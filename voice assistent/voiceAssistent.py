import pyttsx3
import speech_recognition as sr
import datetime
import pyaudio
import  os
import random as rdm
import sys
import time
import pywhatkit
from AppOpener import open
import datetime
import smtplib
import shutil
import requests

thank_list = ["I'm fine, thanks. How about you?","Good, thanks. And you?","I'm good. And yourself?"," I'm doing well, and you?"]


#SAPI5 also known as Microsoft Speech API is the technology for voice recognition and synthesis provided by Microsoft. It can be used to convert Text into Speech.
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')  # getting details of current voice
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def Intro():
    pyttsx3.speak("Hello Raushan, How can i help you")

def AssistentListener():
    none = ""
    #it take input from microphone and return in string format
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recogninzing...")
        works = r.recognize_google(audio, language="en-in")
        print(f"Said : {works}\n")

    except Exception as e:
        print("say that again please...")
        return none
    return works


if __name__=="__main__":
    Intro()

    while True:
        works = AssistentListener().lower()

        if ("dont" in works) or ("don't" in works) or ("not" in works):
            pyttsx3.speak("Type Again")
            print(".")
            print(".")
            continue
        elif (("your" in works) or ("tell" in works)) and ("name" in works):
            speak("I am Assistant of Raushan, i can help you to do some of the limited task till now, and i am still learning ")
        elif ("how are you" in works):
            thank_word = rdm.choice(thank_list)
            speak(thank_word)
        elif ("how are you" in works):
            speak(rdm.choice(thank_list))
        elif ("what is this?" in works):
            speak("i don't know ")
        elif(("what" in works) and ("time" in works)) or (("what's the time") in works):
            current_time = time.strftime("%H:%M:%S", time.localtime())
            speak("it is "+str(current_time ))
        elif "open notepad" in works:
            speak("Opening notepad")
            os.system("notepad")
        elif ("paint" in works) or ("mspaint" in works):
            speak("Opening paint")
            os.system("mspaint")
        
        #App opener 
        elif ("open" in works) and (("msword" or "ms-word" or "word") in works):
            speak("Microsoft word Opening...")
            open("winword", match_closest=True)
        elif ("open" in works) and ("chrome" in works):
            speak("Chrome opening...")
            open("chrome", match_closest=True)
        elif("open" in works) and ("telegram" in works):
            speak("opening telegram...")
            open("telegram", match_closest=True)
        elif("open control panel" in works) or (("open" in works) and ("control" in works)):
            speak("control pannel opening..")
            os.system("control")
        elif("open" in works) and ("cmd" in works or ("command" in works)):
            speak("Command opening...")
            os.system("start cmd")
        
        #create and delete files and folders
        elif (("show" in works) and ("current" in works) and ("folder" or "directory" in works)) or ("show current working directory" in works):
            cwd = os.getcwd()
            speak(f"Current working directory: {cwd}" )
            print(f"Current working directory: {cwd}" )

        elif ("show" in works) and (("folders" in works) or ("folder" in works)):
            speak("all folders list of current working directory are")
            folders_list = os.listdir(os.curdir)
            print(folders_list)
            speak(folders_list)
        #create folder 
        elif ("create" in works) and ("folder" in works):

            pyttsx3.speak("Tell me folder name ")
            ch = AssistentListener()
            if not (os.path.exists("./"+ch+"/")):
                try:
                    os.makedirs('./'+ch+'/')
                    speak("Folder created successfully!")
                    print("Folder created successfully!")
                except:
                    print("Failed to create Folder.")
                    speak("Failed to create Folder.")
            else:
                print("This file already exists, please choose another one!!")
                speak("This file already exists, please choose another one!!")

        elif ("rename folder" in works):
            cwd = os.getcwd()
            os.listdir(cwd)
            pyttsx3.speak("What is folder name")
            previous_name = AssistentListener()
            if previous_name:
                pyttsx3.speak("What is folder new name")
                new_name = AssistentListener()
                os.rename(previous_name,new_name)
                print("folder name changed")
            else:
                print("folder does not exist")
        elif (("remove" in works) or ("delete" in works)) and ("folder" in works):
            cwd = os.getcwd()
            pyttsx3.speak("Which folder you want to delete")
            folder_name = AssistentListener()
            if folder_name in os.listdir(cwd):
                shutil.rmtree(folder_name)
                print(f"{folder_name} removed")
            else:
                print(f"No such {folder_name} found.")
            pyttsx3.speak(f"{folder_name} is deleted successfully")

        
        # music player
        elif ("play" in works) and ("music" in works) or (("play" in works) and ("youtube" in works) ):
            music_list = ['ishare tere','jab koi baat','dil meri na sune','calm down','dheere dheere se meri jingdi','kya baat hai','illigal weapon 2.0']
            music_selected=rdm.choice(music_list)
            speak(f"playing {music_selected}")
            pywhatkit.playonyt(music_selected)


        #send mail and message
        elif ("mail" in works)  or ('email'in works)   or('send email' in works):
            mesg = "Thank you for sending mail"
            print("Sending mail")
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login('login_gmail','gmail_appkey')
            message = mesg
            server.sendmail("sender_email","receiver_mail",message)
            speak("mail sent successfully!")
        
        #google search
        elif(("search" in works) and ("google" in works)):
            speak("Searching on google...")
            pyttsx3.speak("What do you want to search : ")
            target1 = AssistentListener()
            pywhatkit.search(target1)

        elif("movie" in works) and ("list" in works):
            speak("Here is your movie list sir")
            url = "API URL"

            headers = {
                "X-RapidAPI-Key": "HeaderRapidAPI",
                "X-RapidAPI-Host": "RapidPI Host key"
            }

            response = requests.get(url, headers=headers)

            if response.status_code == 200:
                data = response.json()
                if isinstance(data, list):
                    for movie in data:
                        if 'title' in movie:
                            title = movie['title']
                            print(title)
                        else:
                            print("Movie title not found in the response.")
                else:
                    print("Invalid JSON response format. Expected a list.")
            else:
                print("Failed to fetch movie titles. Status code:", response.status_code)


        # close Assistent
        elif ("close yourself" in works) or (("exit" in works) and ("yourself" in works)) or (("close" in works) and ("assistent" or "Assistent" in works)):
            speak("Ok tata bye bye")
            sys.exit()
        else:
            speak("I don't understand ? may be i am Not prepared for this")