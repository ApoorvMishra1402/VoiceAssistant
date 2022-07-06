import pyttsx3 
import speech_recognition as sr 
import datetime 
import wikipedia
import webbrowser
import os
import smtplib
import sys
#from selenium import webdriver

#driver = webdriver.Edge(executable_path="E:\msedgedriver.exe")

engine = pyttsx3.init('sapi5')   #initialising computer voices using sapi5
voices = engine.getProperty('voices') 
#print(voices[1].id)
engine.setProperty('voice', voices[1].id) #using voice 1


def speak(audio):       #function to play computer voice
    engine.say(audio)
    engine.runAndWait()


def wishMe():          #this function is called at the beginning of the code to wish the user 
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  
        speak("how may I help you")       

def takeCommand():
    #   this function takes microphone input from the user and returns string output for the machine
    #   to understand
  
    r = sr.Recognizer()  #initialising a recogniser
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, 1.2)
        print("Listening...")  #setting up thresh hold values to reduce ambient noise
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='e-in')  #using google recognizer to process the audio
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"             #this except block is run when there is no input from the user
    return query

def sendEmail(to, content):   #this function sends an email
    server = smtplib.SMTP('smtp.gmail.com', 587)  #using smtplib to send the email
    server.ehlo()                    
    server.starttls()
    server.login('mishraapoorv2002@gmail.com', 'password')
    server.sendmail('mishraapoorv2002@gmail.com', to, content) #giving credentials of the sender's account
    server.close()

if __name__ == "__main__":   #main driver code
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
           webbrowser.open("youtube.com")
           #driver.get("youtube.com")

        elif 'open google' in query:
            speak('what should i open')
            webbrowser.open("https://in.search.yahoo.com/search?fr=mcafee&type=E211IN826G91504&p=" + takeCommand())

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'play music' in query:
            music_dir = '' #if someone wants to play songs on the computer
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'email' in query:  #sending email
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "apoorv.mishra.20cse@bmu.edu.in"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:     #giving the receiver's credentials and showing an exception 
                                       #in case of faliure
                print(e)
                speak("I'm sorry the E mail wasn't sent successfully")    
        
        elif 'exit code' in query:   #to exit the code 
            speak("Thank's for letting me serve you")
            sys.exit() 

        elif 'playlist' in query: #to start a playlist
            speak("now playing")
            webbrowser.open('https://www.youtube.com/watch?v=tgY1b0AX7B8')   

        elif  'amazon' in query: #to search for products on amazon and flipkart
            speak("what shoud i search for?")
            product = takeCommand()
           
            webbrowser.open('https://www.amazon.in/s?k=' + product + '&ref=nb_sb_noss_1')
        elif  'flipkart' in query:
            speak("what shoud i search for?")
            product = takeCommand()
            
            webbrowser.open('https://www.flipkart.com/search?q=' + product + '&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off')
        elif 'write down' in query:
            speak("What should I write down?")
            content = takeCommand()    
            print(content)
        elif 'search' in query:   #to search for queries on the internet
            speak("what should i search for")
            new_query = takeCommand()
            webbrowser.open("https://www.bing.com/search?q=" + new_query)
        elif 'word document' in query:  #to write and save text in a word file (still buggy)
            os.open('./Word Document')
            
       
