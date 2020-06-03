import pygame
from gtts import gTTS

text="Hello Python Text to Speech Tutorial"

language="en"


obj=gTTS(text=text,lang=language,slow=False)
obj.save("audio.mp3")

pygame.mixer.init()
pygame.mixer.music.load(open("audio.mp3","rb"))
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    print("Playing..")

print("Played")