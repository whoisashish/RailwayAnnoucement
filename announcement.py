import os
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS

def textToSpeech(text, filename):
    mytext = str(text)
    language = 'hi'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save(filename)
   
def mergeAudios(audios):
    combined = AudioSegment.empty()
    for audio in audios:
        combined+=AudioSegment.from_mp3(audio)
    return combined

def generateSkeleton():
    audio = AudioSegment.from_mp3('railway.mp3')

    start = 87100
    finish = 90200
    audioProcessed = audio[start:finish]
    audioProcessed.export("hindi_1.mp3",format="mp3")

    start = 91000
    finish = 92200
    audioProcessed = audio[start:finish]
    audioProcessed.export("hindi_3.mp3",format="mp3")

    start = 94000
    finish = 95000
    audioProcessed = audio[start:finish]
    audioProcessed.export("hindi_5.mp3",format="mp3")

    start = 96000
    finish = 98900
    audioProcessed = audio[start:finish]
    audioProcessed.export("hindi_7.mp3",format="mp3")

    start = 105500
    finish = 108200
    audioProcessed = audio[start:finish]
    audioProcessed.export("hindi_9.mp3",format="mp3")

    start = 109000
    finish = 112250
    audioProcessed = audio[start:finish]
    audioProcessed.export("hindi_11.mp3",format="mp3")

def generateAnnouncement(filename):
     df = pd.read_excel(filename)
     print(df)
     for index, item in df.iterrows():
         textToSpeech(item['from'], 'hindi_2.mp3')

         textToSpeech(item['via'], 'hindi_4.mp3')

         textToSpeech(item['to'], 'hindi_6.mp3')

         textToSpeech(item['train_no'] + " " + item['train_name'], 'hindi_8.mp3')

         textToSpeech(item['platform'], 'hindi_10.mp3')

         audios = [f"hindi_{i}.mp3" for i in range(1,12)]

         announcement = mergeAudios(audios)
         announcement.export(f"announcement_{index+1}.mp3", format="mp3")


if __name__=="__main__":
    print("Generating Skeleton....")
    generateSkeleton()
    print("Now generating Announcement....")
    generateAnnouncement("announce_hindi.xlsx")

