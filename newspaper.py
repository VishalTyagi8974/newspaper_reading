import requests
import json

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")

    speak.Speak(str)



if __name__ == '__main__':
    speak('news for today is...')
    url="get a api from newsapi.org"
    news= requests.get(url).text
    newss= json.loads(news)

    print(newss["articles"])
    arts = newss["articles"]
    for articles in arts:
        speak(articles["title"])