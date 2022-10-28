import speech_recognition as sr
import gtts
from playsound import playsound
import os
import tkinter as tk
from tkinter import messagebox as mb

#Assigning variables
act_cmd = "hi python"

#Speech recognizer 
r = sr.Recognizer()

#Functions
def get_audio():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print("Listening...")
        audio = r.listen(source)
    return audio

def audio_to_text(audio):
    text = ""
    try:
        text = r.recognize_google(audio)
    except sr.UnknownValueError:
        print("Couldn't understand what you said there")
    except sr.RequestError:
        print("Google acting up again!")
    return text

def play_sound(text):
    try:
        tts = gtts.gTTS(text)
        tempfile = "./myaudio.mp3"
        tts.save(tempfile)
        playsound(tempfile)
        os.remove(tempfile)
    except AssertionError:
        print("Couldn't play the sound man!")
    return

while True:
    a = get_audio()
    command = audio_to_text(a)
    print(command)
    if act_cmd in command.lower():
        play_sound("What can i do for you")
        note = get_audio()
        note = audio_to_text(note)
        if note:
            play_sound(note)
            print("noted")
    if "bye bye" in command.lower():
        play_sound("Goodbye!")
        break
    else:
        play_sound("I don't know what to do for that")

print("Code ran successfully!")