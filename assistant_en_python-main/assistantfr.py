import pywhatkit
import speech_recognition as sr
import pyttsx3 as ttx
import datetime
import random
import wakeonlan
import webbrowser
from tkinter import *
from playsound import playsound
import pyautogui
import os




listener=sr.Recognizer()
engine=ttx.init()

voice=engine.getProperty('voices')
engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US-FR_DAVID_11.0')
engine.setProperty("rate", 175)
new_vol = 1
engine.setProperty("volume", new_vol)

def parler(text):
        engine.say(text)
        engine.runAndWait()

def arret():
    pyautogui.press("Ctrl", "f2")


def tv():
    wakeonlan.send_magic_packet('44:ef:bf:de:fd:9b')

def quantique():
    uri = "https://www.google.com/search?q=ordinateur+quantique&biw=1166&bih=617&tbm=nws&sxsrf=APq-WBsnWavHUN_9CLWIGXwVszz6QQA2ug%3A1643740145265&ei=8Xv5YevaD_LjsAeWk7y4Ag&oq=ordinate&gs_lcp=Cgxnd3Mtd2l6LW5ld3MQARgCMggIABCABBCxAzIICAAQgAQQsQMyCwgAEIAEELEDEIMBMggIABCABBCxAzIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDoECAAQQzoICAAQsQMQgwE6BQgAELEDUP-yAVjHvAFggdABaANwAHgAgAGSAYgBjgeSAQM2LjOYAQCgAQGwAQDAAQE&sclient=gws-wiz-news"
    webbrowser.open(uri)



def ecouter():

        while True:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Je vous ecoute..")
                audio = r.listen(source, timeout=1, phrase_time_limit=5)

            try:
                print("Reconnaisance...")
                Query = r.recognize_google(audio, language="fr-FR")
                print(f"Vous avez dit: {Query}")

            except Exception as e:

                return ""
            return Query

def lancer_assistant():

        while True:
            #test

            command=ecouter()
            print(command)

            if 'mets la chanson de ' in command:
                chanteur=command.replace("mets la chanson de", "")
                pywhatkit.playonyt(chanteur)

            elif 'heure' in command:
                heure=datetime.datetime.now().strftime('%H:%M')
                parler('il est'+heure)

            elif "allume la tv" in command or "allume tv" in command or 'allume tele' in command or 'allume la télé' in command :
                tv()

            elif "recherche Quantique " in command or "recherche quantique" in command:
                quantique()

            elif "stop" in command:
                arret()

            elif "calculatrice" in command or "lance la calculatrice" in command:
                path_2 = "C:\\Windows\\System32\\calc.exe"
                webbrowser.open(path_2)

            elif "notepad"in command or "lance Notepad" in command:
                path_1 = "C:\\Windows\\System32\\notepad.exe"
                webbrowser.open(path_1)


            else:
                print('je ne comprends pas')



def papi():
        exit()



while True:
        lancer_assistant()


