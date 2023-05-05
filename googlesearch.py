import speech_recognition as sr
import webbrowser as wb
from assistantanswer import tts

chrome_path='C:/Program Files (x86)/Google/Chrome/Applications/chrome.exe %s'
r=sr.Recognizer()

with sr.Microphone() as source:
      print('Please ask the topic for the google search: ')
      audio=r.listen(source)
      print('Okay.')

try:
      text=r.recognize_google(audio)
      print('You asked this: \n' + text)
      lang='en'

      speak.tts(text, lang)

      f_text='https://www.google.com/search?q='+text
      wb.get(chrome_path).open(f_text)

except Exception as e:
      print(e)
