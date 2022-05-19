import pyttsx3  
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import random
import requests
import pywhatkit as kit
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtCore import QTimer,QTime,QDate,Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import*
from PyQt5.QtGui import*
from PyQt5.QtWidgets import*
from PyQt5.uic import loadUiType
from  rambofrontui import Ui_MainWindow
import sys
import winshell


    
    

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)

engine.setProperty('rate', 190)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon  Sir!")

    else:
        speak("Good Evening Sir!")

    speak("I am Rambo! . Created By yatin and abhinav singh...Please tell me how may I help you")
    
    
class MainThread(QThread):
     def __init__(self):
          super(MainThread, self).__init__()
     
     def run(self):
          self.Execution()
          
              
    

     def takeCommand(self):
          # It takes microphone input from the user and returns string output

          r = sr.Recognizer()
          with sr.Microphone() as source:
             print("Listening...")
             r.pause_threshold = 1
             r.energy_threshold = 500
             audio = r.listen(source)

          try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")

          except Exception as e:
          
               print("Say that again please...")
          
               return "None"
          return query





     def Execution(self):
          wishMe()
          while True:
                 
         
             self.query = self.takeCommand().lower()

           
             if ('wikipedia' in self.query):
                speak('Searching Wikipedia...')
                self.query = self.query.replace("wikipedia", "")
                result = wikipedia.summary(self.query, sentences=2)
                speak("According to Wikipedia")
                speak(result)
                print(result)
     


           

             elif ('open google' in self.query):
                speak("Ok sir..!")
      
                speak("Sir what should i search for you on google..")
                self.cm=self.takeCommand().lower()
     
                webbrowser.open(f"{self.cm}")
                speak("Ok sir as your wish...")

             elif ('open stackoverflow' in self.query):
                webbrowser.open("stackoverflow.com")

             elif ('music' in self.query):
                speak("ok sir wait a while....")
                music_dir = 'C:\\Users\\admin\\OneDrive\\Desktop\\videos\\mp3'
                songs = os.listdir(music_dir)
                print(songs)
                r = random.randint(0, len(songs)-1)

                os.startfile(os.path.join(music_dir, songs[r]))

             elif ('time' in self.query):
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strTime}")
                print(strTime)

             elif ('code' in self.query):
                codePath = "C:\\Users\\admin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)

             elif ('chandigarh university ' in self.query):
                webbrowser.open("uims.cuchd.in")
     

             elif ('blackboard ' in self.query):
                webbrowser.open("cuchd.blackboard.com")

             elif ('thank you' in self.query):
                speak("Your Welcome sir ....my pleasure...! Any other Request?")
     

             elif (' video' in self.query):
                speak("OK sir wait a while....")
                vid_dir = 'C:\\Users\\admin\\OneDrive\\Desktop\\videos'
                videos = os.listdir(vid_dir)
                print(videos)
                ran = random.randint(0, len(videos)-1)
                os.startfile(os.path.join(vid_dir, videos[ran]))
        
             elif('exit'in self.query):
                speak("Thankyou Sir for your  time.....Good bye...Best wishes for the day! ahead")
                break
    
             elif('command prompt'in self.query):
                path='C:\\WINDOWS\\system32\\cmd.exe'
                os.startfile(path)
        
             elif('ip address'in self.query):
                speak("ok Sir..")
                from requests import get
                ip =get('https://api.ipify.org/').text
                speak(f"Your Ip address is {ip}")
                print(ip)
    
    
               # sending message on whatsapp
    
    
             elif('send message'in self.query):
                speak("Ok sir whatsapp web is opening in few seonds")
                web='https://web.whatsapp.com/'
                webbrowser.open(web)
                speak("Tell me the person name  whom you want to send message..")
                self.person= self.takeCommand()
       
        
        
                if('Abhinav'in person):
            
                     speak("Tell me the message sir..")
                     self.message=self.takeCommand().lower()
           
                     kit.sendwhatmsg_instantly('+91 60055 89567', message,4)
             
                elif('Vinay'in self.person):
                     speak("Tell me the message sir..")
                     self.message=self.takeCommand().lower()
                     kit.sendwhatmsg_instantly('+91 9501162294', message,4)
            
                elif('Tanish'in self.person):
                      speak("Tell me the message sir..")
                      self.message=self.takeCommand().lower()
                      kit.sendwhatmsg_instantly('+91 6283 587 861', message,4)
        
                elif('Kartik 'in self.person):
                     speak("Tell me the message sir..")
                     self.message=self.takeCommand().lower()
                     kit.sendwhatmsg_instantly('+91 78149 58829', message,4)
            
            
                elif('Sourav'in self.person):
                     speak("Tell me the message sir..")
                     self.message=self.takeCommand().lower()
                     kit.sendwhatmsg_instantly('+91 96463 93982', message,4)
           
                else:
                     speak("Sorry sir not in my program...yet")
            
            
            
            
            
            
        
             elif('youtube' in self.query or'open youtube'in self.query):
                speak("ok Sir Tell me  what should  i play on youtube...")
                self.video=self.takeCommand().lower()
                kit.playonyt(self.video)
                speak("Ok sir as your wish...")
            
             elif("screenshot"in self.query):
                speak('Ok sir wiat a while taking Screen shot')
                kit.take_screenshot()
             
            
             elif(' joke'in self.query):
                import pyjokes
                joke=pyjokes.get_joke()
                speak(joke)
        
            
             elif("shut down the system"in self.query):
                 speak("Ok sir the system is shutting down in few seconds")
                 os.system('shutdown /s /t 5')
        
      
             elif('Restart the system 'in self.query):
                speak("Ok sir the system is restarting in few seconds")
                os.system('shutdown /r /t 5')
        
             elif('open disney plus 'in self.query):
                 web="https://www.hotstar.com/in"
                 webbrowser.open(web)
                 speak("Ok sir  as youer wish")
        
             elif('facebook 'in self.query):
                web="https://www.facebook.com/"
                webbrowser.open(web)
         
             elif('play movie'in self.query):
                speak("Ok sir wait a while..")
                movie_dir="C:\\Users\\admin\\OneDrive\\Desktop\\videos\\movies"
                movie = os.listdir(movie_dir)
                ran=random.randint(0, len(movie)-1)
                os.startfile(os.path.join(movie_dir,movie[ran]))
    
             elif('hello 'in self.query):
                 speak("Hello  Sir! Tell me your name")
                 self.name= self.takeCommand()
                 speak(f"Hello, {name} and I'm Rambo  How can i help you. ")
        
             elif('how are you 'in self.query ):
                 speak('I am fine Sir How are you ?')
                 self.take=self.takeCommand()
                 if('good'in self.take or 'fine' in self.take):
                         speak('Nice sir How can i help you then...')
                 elif('not good'in self.take or 'not fine'in self.take):
                      speak('Tell me your Problem sir ..if i can solve it..')
                 else:
                         speak('Did not get you sir ..')
                         
             
             elif ('empty recycle bin' in self.query):
                winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
                speak("Recycle Bin Recycled")
                
             elif('Thats good'or'nice'in self.query):
                speak("My Pleasure Sir ...Any other Request..")
                     
                     
              
             
    
             
             else:
                 speak("Sorry sir could not understand..")
       
       


     
class Main(QMainWindow):
     def __init__(self):
          super().__init__()
          self.ui=Ui_MainWindow()
          self.ui.setupUi(self)  
          self.ui.pushButton.clicked.connect(self.startTask)
          self.ui.pushButton_2.clicked.connect(self.close)
    
     def startTask(self):
          self.ui.movie=QtGui.QMovie(".\\pics/maxresdefault.jpg")
          self.ui.label.setMovie(self.ui.movie)
          self.ui.movie.start()
          startExecution.start()
          

        
    



if __name__ =="__main__":
     startExecution=MainThread()
     app=QApplication(sys.argv)
     rambo=Main()
     rambo.show()
     exit(app.exec_())
     



