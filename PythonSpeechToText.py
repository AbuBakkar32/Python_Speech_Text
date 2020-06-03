import speech_recognition as speech

audio_text=""

read_audio=speech.Recognizer()
with speech.Microphone() as input_source:
    print("Speak : ")
    audio=read_audio.listen(input_source)


try:
    audio_text=read_audio.recognize_google(audio)
    print("You Said : "+audio_text)
except:
    print("Error Occured")

