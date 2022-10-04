#SpeechRecog.python
#2022-10-02 ver
#https://prlabhotelshoe.tistory.com/8?category=995004

import speech_recognition as sr

r = sr.Recognizer()

# audio_file = sr.AudioFile('./test_file.wav')
audio_file = sr.AudioFile('./news.wav')

with audio_file as source:
    audio = r.record(source)


#sys.stdout = open('stdout.txt','w')
f = open("output.txt",'w')
# f.close()

Txt = r.recognize_google(audio,language = 'ko-KR')


print(Txt)
f.write(Txt)
# sys.stdout.close()



#자 이게 보여야 정상입니다아
##아니 이게 왜 안되는거야