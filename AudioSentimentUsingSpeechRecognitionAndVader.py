# pip install vadersentiment
# pip install SpeechRecognition

# References:
# https://stackoverflow.com/questions/52283840/i-cant-install-pyaudio-on-windows-how-to-solve-error-microsoft-visual-c-14
# https://pypi.org/project/SpeechRecognition/2.1.3/

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import speech_recognition as sr 

recognizer=sr.Recognizer()
with sr.Microphone() as source: 

    print('Clearing background noise...')
    recognizer.adjust_for_ambient_noise(source,duration=1)
    print('Waiting for your message...')
    recordedaudio=recognizer.listen(source)
    print('Done recording..') 
try:
    print('Printing the message..')
    text=recognizer.recognize_google(recordedaudio,language='en-US')
    print('Your message:{}'.format(text))
except Exception as ex:
    print(ex)
#Sentiment analysis

Sentence=[str(text)]
analyser=SentimentIntensityAnalyzer()
for i in Sentence:
    v=analyser.polarity_scores(i)
    print(v) 