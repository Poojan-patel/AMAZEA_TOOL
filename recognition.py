import speech_recognition as s_r
import webbrowser
# from googletrans import Translator
# from langdetect import detect
# webbrowser.open('https://google.com/?#q=Youtube',new=3)
try:
	from googlesearch import search 
except:
	print("Not a package:")
print(s_r.__version__) # just to print the version not required
r = s_r.Recognizer()
my_mic = s_r.Microphone(device_index=1) #my device index is 1, you have to put your device index
with my_mic as source:
    print("Say now!!!!")
    r.adjust_for_ambient_noise(source) #reduce noise
    a1=r.listen(source)

final=r.recognize_google(a1)
print(final)