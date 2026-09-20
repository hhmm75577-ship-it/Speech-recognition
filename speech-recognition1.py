import pyttsx3
import speech_recognition as sr
#import torch
#from playsound import playsound
#import os
#from psutil import users
#from transformers import AutoTokenizer, AutoModelForCausalLM
from huggingface_hub import InferenceClient
# Prefer environment variables or huggingface-cli login over plain text strings!
#import json
import pygame
import pyttsx3 as ss
import time
from gtts import gTTS
engine = pyttsx3.init()
pygame.mixer.init()
token = "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"
client = InferenceClient("Qwen/Qwen2.5-1.5B-Instruct", token=token)
rec = sr.Recognizer()
while True:
    with sr.Microphone() as src:
        audio = rec.listen(src)
        text = rec.recognize_google(audio)
        print(text)
    #user = input("Enter your message: ")
    messages = [
    {"role": "user", "content": text},
    ]
    try:


        response =client.chat_completion(messages=messages, max_tokens=256)

        ai =response.choices[0].message.content
        print(f'AI: {ai}')
        tts = gTTS(text=ai, lang='en')
        tts.save('ai.mp3')

        pygame.mixer.music.load('ai.mp3')
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)
        pygame.mixer.music.unload()
    except Exception as e:
        print(f"An error occurred: {e}")

