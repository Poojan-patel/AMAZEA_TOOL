#!/usr/bin/env python
# coding: utf-8

# In[8]:


import cv2
import webrecognize
import sys
from tkinter import *
import tkinter as tk 
import signup as sp
def face_reco_done_or_not():
    mw.destroy()
    args=["","frontfacial.xml","./Known/"]
    name, frame = webrecognize.function_for_face_reco(args)
    if(name == 'No'):
        var = sp.main()
        cv2.imwrite(filename=var, img=frame)
    else:
        print("Found")

def fun():
    video_capture = cv2.VideoCapture(0)

    while True:
        ret, frame = video_capture.read()
        cv2.imshow('Face_Reco', frame)
        if (cv2.waitKey(1) & 0xFF == ord('q')):
            break
    video_capture.release()
    cv2.destroyAllWindows()

mw = tk.Tk()
mw.title('AMAZEA')
mw.configure(background='turquoise')
mw.geometry("500x500")
lbl = tk.Label(mw, text='Welcome to Lightning Parties!', fg='purple', bg='turquoise', font=('comicsans', 14))
lbl.pack()

btn = tk.Button(mw,text="Face Recognition",command=face_reco_done_or_not)
btn.pack()

mw.mainloop()


# In[ ]:




