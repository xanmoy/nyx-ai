import speech_recognition as sr
import os
import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")
while 1:
    print("Hello Sir, I am Nyx, a Virtual Assistant based on Source Language Model for Dialogue Applications, I was created by Mr. Tanmoy Ganguly, I am Here to assist you")
    s = input()
    speaker.Speak(s)