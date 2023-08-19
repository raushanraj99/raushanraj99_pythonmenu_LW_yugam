# function importing
from tkinter import *
import tkinter as tk
from tkinter.ttk import *
from time import strftime
import datetime as dt
import os
import pywhatkit 
import smtplib
import vonage
import random as rdm
import boto3 as bt
from instabot import Bot
from googlesearch import search
from geopy.geocoders import Nominatim
import numpy as np
import cv2

#tkinter window dimension
root = Tk()
root.title('Yugam')
root.geometry("1500x900")
root.resizable(True, True)

# menu functions : 

def CreateFolder():
    ch = input("Folder name : ")
    if not (os.path.exists("./"+ch+"/")):
        try:
            os.makedirs('./'+ch+'/')
            print("Folder created successfully!")
        except:
            print("Failed to create Folder.")
    else:
        print("This folder already exists, please choose another one!!")
def currentDirectory():
    cwd = os.getcwd()
    value=cwd
    display.config(text=value)

def showAllfolder():
    # global folders_list
    folders_list = os.listdir(os.curdir)
    value = folders_list
    display.config(text=value)

def instanceLaunch():
    myec2 = bt.client("ec2")
    response = myec2.run_instances(ImageId = "Your_Image_id",
        InstanceType = "t2.micro",
        MaxCount=1,
        MinCount=1,
        TagSpecifications=[
                {
                    'ResourceType': 'instance',
                    'Tags': [
                        {
                            'Key': 'Name',
                            'Value': "teamyugam1" # teamyugam is the InstanceName
    },]},])
    value = "instance Launched"
    display.config(text=value)
    print(response)

def s3Launch():
    S3 = boto3.client('s3')

    response = S3.create_bucket( 
        ACL = 'private',
        Bucket= 'myyugamteam1221',
         CreateBucketConfiguration={
              "LocationConstraint":"ap-south-1"
         }
    )
    value = "S3 Launched"
    display.config(text=value)
    
def aboutYugam():
    value = " We are The Creator from project code 100 "
    display.config(text=value)

    
# Creating Menubar
menubar = Menu(root)

# Adding File Menu and commands
file = Menu(menubar, tearoff = 0, font=("Arial", 15))
menubar.add_cascade(label ='File', menu = file)
file.add_command(label ='New Folder', command = CreateFolder)
file.add_command(label ='Current folder', command = currentDirectory)
file.add_command(label ='show Folders', command = showAllfolder)
#file.add_command(label ='Save', command = None)
file.add_separator()
file.add_command(label ='Exit',background="#FF0000", command = root.destroy)

# Adding Edit Menu and commands
aws = Menu(menubar, tearoff = 0, font=("Arial", 15))
menubar.add_cascade(label ='AWS', menu = aws)
aws.add_command(label ='Instance Launch', command = instanceLaunch)
aws.add_command(label ='S3 Launch', command = s3Launch)


# Adding Help Menu
about = Menu(menubar, tearoff = 0, font=("Arial", 15))
menubar.add_cascade(label ='About', menu = about)

about.add_separator()
about.add_command(label ='About Yugam',background="#00FF00", command = aboutYugam)

#variable 
datetime = dt.datetime.now()
timedt = datetime.strftime("%c")

lbl = tk.Label(root, text="Team Yugam", font=("Helvetica bold", 40), fg='#f00').pack(pady=15,padx=5)
lbl2= tk.Label(root,text=" %s"%timedt,font=("Helvetica bold",15)).place(y=30,x=1150)


#notebook
display = tk.Label(root, height=3, width = 100, bg="#f00",fg="#FFFFFF", text="",font=("Arial",15)) 
display.pack()
value = ""

# pass function for displaying data 
thank_list = ["I'm fine, thanks. How about you?","Good, thanks. And you?","I'm good. And yourself?"," I'm doing well, and you?"]
final_list = rdm.choice(thank_list)

#all function
def welcome(thank_list):
    value = thank_list
    display.config(text=value)

def SayHello():
    value="Hello from team Yugam "
    display.config(text=value)

def openNotepad():
    value="Opening notepad done "
    display.config(text=value)
    os.system('notepad')
    
def openmspaint():
    value="Opening paint done "
    display.config(text=value)
    os.system('mspaint')

def openmsword():
    os.system("start winword")
    value="Opening Ms-Word Done"
    display.config(text=value)
    
def openchrome():
    os.system("start chrome")
    value="opening chrome done"
    display.config(text=value)

def commandprompt():
    value="Opening Control pannel done "
    display.config(text=value)
    os.system("start cmd")
    

#folder creation

#music player
def ytmusicplay():
    musicList=["ishare tere",'jab koi baat','dil meri na sune','calm down','dheere dheere se meri jindgi','kya baat hai','illigal weapon 2.0']
    final_music= rdm.choice(musicList)
    value=f"played {final_music} "
    display.config(text=value)
    pywhatkit.playonyt(final_music)

def sendEmail():    
    mesg = "This is your message"
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('Sender_email','Sender_app_password')
    message = mesg
    server.sendmail("sender_email","receiver_email",message)
    value="email sent"
    display.config(text=value)

def googleSearch(): # open google and search the following text.
    print("searaning")
    searchvalue="linux world"
    pywhatkit.search(searchvalue)
    value="google search done"
    display.config(text=value)

def sendSMS():
    value = ""
    success = " Message sent successfully "
    
    client = vonage.Client(key="vonage_key", secret="vonage_secret_key")
    sms = vonage.Sms(client)

    responseData = sms.send_message(
        {
            "from": "Vonage APIs",
            "to": "receiver_number",
            "text": "Hello Buddy how are you",
        }
    )
    if responseData["messages"][0]["status"] == "0":
        value = success
        display.config(text=value)
    else:
        value = f"Message failed with error: {responseData['messages'][0]['error-text']}"
        display.config(text=value)
        print(f"Message failed with error: {responseData['messages'][0]['error-text']}")
def instapost():
    bot = Bot()
    bot.login(username='insta_userName', password='InstaidPassword',  use_cookie=False, ask_for_code=True)
    bot.upload_photo('snake_ladder.jpg', caption='this post is created by instagram')
    value="insta post done"
    display.config(text=value)

def googleSearchindisplay():
    global value
    query = input("Enter search : ")
    for i in search(query,stop=5,num=5):
        print(i)
        value = i
        display.config(text=value)
        
def searchboxmap():
    geolocator = Nominatim(user_agent="location_details")
    location = geolocator.geocode("Jaipur")
    lat = location.latitude
    long= location.longitude
    value =[lat,long]
    display.config(text=value)
        
def createimage():
    image = np.zeros((450, 600,3),dtype=np.uint8) *255

    saffron_color = (51, 153,255)  # Saffron color (RGB: 255, 153, 51)
    white_color = (255, 255, 255)   # White color (RGB: 255, 255, 255)
    green_color = (8,136,19)
    blue_color = (128,0,0)

    height = image.shape[0] // 3

    image[0:height, : ] = saffron_color
    image[height:height*2, : ] = white_color
    image[height*2:, : ] = green_color

    #Ashoka chakra
    cv2.circle(image, (300, 225), 78, blue_color, -1)

    cv2.imshow("image ",image)
    cv2.waitKey()
    cv2.destroyAllWindows()
    
    value = "indian flag created"
    display.config(text=value)

def videocamera():
    video = cv2.VideoCapture(0)
    while True:
        ret, photo= video.read()
        cv2.imshow("NEWS",photo)
        if cv2.waitKey(30)==13:
            break
    cv2.destroyAllWindows()
    value = "Camera opened"
    display.config(text=value)
    
def movielist():
    # 3. movie list
    titles = []
    import requests
    url = "Api_url"

    headers = {
        "X-RapidAPI-Key": "Your_api_key",
        "X-RapidAPI-Host": "Movie_api_host"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if isinstance(data, list):
            
            for movie in data:
                if 'title' in movie:
                    title = movie['title']
                    print(title)
                    titles.append(title)
                    display.config(text=titles)
                else:
                    print("Movie title not found in the response.")

        else:
            print("Invalid JSON response format. Expected a list.")
    else:
        print("Failed to fetch movie titles. Status code:", response.status_code)

        
def whatsmesg():
    # 2. multiple message on whatapps

    import pyautogui as p
    import time
    time.sleep(6)

    for i in range(10):
        p.typewrite("Hi bro")
        p.press("enter")

    print("message sent")
    value = "Whatapps done"
    display.config(text=value)
    

#exit from the window
def exit():
    value="Exit done"
    display.config(text=value)
    root.quit()

    #All Button
btn = tk.Button(root, text="How are you ? ", width="30", height="3",fg="#FFFFFF",bg="#00FF00",font=("Arial",15,"bold"),command=lambda:welcome(final_list)).place(x=550,y=280)
btn = tk.Button(root, text="Say hello", width="20", height="2",fg="#FFFFFF",bg="#00008B",command=SayHello).place(x=30,y=430)
btn = tk.Button(root, text="Open Notepad", width="20", height="2",fg="#FFFFFF",bg="#00008B",command=openNotepad).place(x=210,y=430)
btn = tk.Button(root, text="Open ms-paint", width="20", height="2",fg="#FFFFFF",bg="#00008B",command=openmspaint).place(x=390,y=430)
btn = tk.Button(root, text="Open Ms-Word", width="20", height="2",fg="#FFFFFF",bg="#00008B",command=openmsword).place(x=570,y=430)
btn = tk.Button(root, text="Open Chrome", width="20", height="2",fg="#FFFFFF",bg="#00008B",command=openchrome).place(x=750,y=430)
btn = tk.Button(root, text="command prompt", width="20", height="2",fg="#FFFFFF",bg="#00008B",command=commandprompt).place(x=930,y=430)
btn = tk.Button(root, text="YouTube music", width="20", height="2",fg="#FFFFFF",bg="#00008B",command=ytmusicplay).place(x=1110,y=430)
btn = tk.Button(root, text="Send Mail", width="20", height="2",fg="#FFFFFF",bg="#00008B",command=sendEmail).place(x=1290,y=430)
btn = tk.Button(root, text="Google Search", width="20", height="2",fg="#FFFFFF",bg="#00008B",command=googleSearch).place(x=30,y=510)
btn = tk.Button(root, text="Send SMS", width="20", height="2",fg="#FFFFFF",bg="#00008B",command=sendSMS).place(x=210,y=510)
btn = tk.Button(root, text="Instagram Post", width="20", height="2",fg="#FFFFFF",bg="#00008B",command=instapost).place(x=390,y=510)
btn = tk.Button(root, text="Google result", width="20", height="2",fg="#FFFFFF",bg="#00008B",command=googleSearchindisplay).place(x=570,y=510)
btn = tk.Button(root, text="search map", width="20", height="2",fg="#FFFFFF",bg="#00008B",command=searchboxmap).place(x=750,y=510)

btn = tk.Button(root, text="Create image", width="20", height="2",fg="#FFFFFF",bg="#00008B",command=createimage).place(x=930,y=510)
btn = tk.Button(root, text="Camera", width="20", height="2",fg="#FFFFFF",bg="#00008B",command=videocamera).place(x=1110,y=510)
btn = tk.Button(root, text="Movie list", width="20", height="2",fg="#FFFFFF",bg="#00008B",command=movielist).place(x=1290,y=510)
btn = tk.Button(root, text="WhatsApp msg", width="20", height="2",fg="#FFFFFF",bg="#00008B",command=whatsmesg).place(x=30,y=590)


# lbl = tk.Label(root, text="Music System",fg="#ffffff",bg="#000000").pack(pady=3)
btn = tk.Button(root, text="Exit", width="30", height="3",fg="#FFFFFF",bg="#FF0000",command=root.destroy).pack(side=BOTTOM)

# display Menu
root.config(menu = menubar)
mainloop()