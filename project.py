#!/usr/bin/env python
# coding: utf-8

# In[19]:


#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import speech_recognition as s_r
import webbrowser
from googletrans import Translator
from langdetect import detect
import goslate
# webbrowser.open('https://google.com/?#q=Youtube',new=3)
def main(s,d):
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
    #     print("Say the base language:")
    #     audio1 = r.listen(source) #take voice input from the microphone
    #     print("Say the language in which you want to translate:")
    #     audio2 = r.listen(source)
        print("Say the statement")
        audio = r.listen(source)

    trans = Translator()
    # print(audio1)
    # print(audio2)
    # d = detect(r.recognize_google(audio2))
    # s = detect(r.recognize_google(audio1))
    # print(s)
    # print(d)
    #gs = goslate.Goslate()
    final = r.recognize_google(audio)
    x = trans.translate(final,src=s,dest=d)
    print(final)
    print(x.text)
    return final,x.text
    #webbrowser.open('https://google.com/?#q='+str(x),new=2)

    # trans = Translator()
    # t = trans.translate('Hello how are you?',src='en',dest='ja')
    # print(f'{t.text}')
    # print(t.origin)

#main('en','gu')

