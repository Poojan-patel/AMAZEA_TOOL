import cv2
import webrecognize
import sys
from tkinter import *
import tkinter as tk 
import signup_updated as sp
import speech_main as sm
def face_reco_done_or_not():
    mw.destroy()
    args=["","frontfacial.xml","./Known/"]
    name, frame = webrecognize.function_for_face_reco(args)
    if(name == 'No'):
        var = args[2]+sp.main()
        cv2.imwrite(filename=var, img=frame)
        res=var[:-(4)]
        res=(res.split("/"))[-1]
        #print(res+" a")
        sm.main(res)
    else:
        print("Found")
        res=name
        sm.main(res)

mw = tk.Tk()
mw.title('AMAZEA')
mw.configure(background='turquoise')
mw.geometry("600x200")
lbl = tk.Label(mw, text='Amazea : Face and Speech recognition and translation...', fg='purple', bg='NavajoWhite', font=('comicsans', 15))
lbl.place(x=50,y=20)

btn = tk.Button(mw,text="Face Recognition",command=face_reco_done_or_not,bg='SkyBlue3',font=10,fg='RoyalBlue3')
btn.place(x=215,y=100)

mw.mainloop()
