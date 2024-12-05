import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Adjusting for ambient noise...")
    recognizer.adjust_for_ambient_noise(source)
    print("Listening for audio...")
    audio = recognizer.listen(source)

print("Audio captured successfully!")
