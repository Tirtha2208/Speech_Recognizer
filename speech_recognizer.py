import speech_recognition as sr

AUDIO_FILE=("sample.wav")

r=sr.Recognizer()

with sr.AudioFile(AUDIO_FILE) as source:
  audio=r.record(source)

try:
  print("The Audio says that:")
  print(r.recognize_google(audio))
except sr.UnknownValueError:
  print("Sorry We couldn't understand the speech")
except sr.RequestError:
  print("Sorry we couldn't be able to fetch the result")