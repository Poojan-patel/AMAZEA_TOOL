from tkinter import *
import tkinter as tk
from PIL import ImageTk ,Image
from tkinter.ttk import *
import project as pu
from translate import Translator
lan1=""
lan2=""
dic={'English':'en','Italian':'it','Gujarati':'gu','Portuguese':'pt','French':'fr','Hindi':'hi','German':'de'}
def main(name):
    def change_dropdown1(*args):
        global lan1
        lan=v1.get()
        lan1=lan
        #print(lan1)
    def change_dropdown2(*args):
        global lan2
        lan=v2.get()
        lan2=lan
        #print(lan2)
    def speech_work():
        global lan1
        global lan2
        print(lan1,lan2)
        print(dic[lan1],dic[lan2])
        ans1,ans2=pu.main(dic[lan1],dic[lan2])
        translator= Translator(from_lang=dic[lan2],to_lang=dic[lan1])
        ans1 = translator.translate(ans2)
        #print(ans1+" kk")
        l6=tk.Label(mw3,text="",bg='deepskyblue2')
        l6.config(height=10,width=500)
        l6.place(x=150,y=320)
        l4=tk.Label(mw3,text=ans1,font=('Helvetica',20),bg='plum3')
        l4.place(x=150,y=320)
        l5=tk.Label(mw3,text=ans2,font=('Helvetica',20),bg='plum3')
        l5.place(x=150,y=370)
        print(ans1,ans2)

    mw3=tk.Tk()
    mw3.title("Speech Recognization and Translation")
    mw3.configure(background='deepskyblue2')
    mw3.geometry("700x600")

    fname="Welcome "+name+"..."
    l1=tk.Label(mw3,text=fname,font=('comicsans', 20),bg='lavender',fg='PaleVioletRed4')
    l1.place(x=170,y=25)

    v1=StringVar(mw3)
    v2=StringVar(mw3)
    v1.set('--choose language--')
    v2.set('--choose language--')

    pm1 = OptionMenu(mw3,v1,'--choose language--','English','Gujarati','German','Portuguese','Italian','French')
    pm2 = OptionMenu(mw3,v2,'--choose language--','English','Gujarati','German','Portuguese','Italian','French','Hindi')
    l2=tk.Label(mw3, text="Base language :",font=('Helvetica',13),bg='plum3')
    l2.place(x=100,y=100)
    l3=tk.Label(mw3, text="Translation language :",font=('Helvetica',13),bg='plum3')
    l3.place(x=59,y=160)
    pm1.place(x=250,y=100)
    pm2.place(x=250,y=160)

    v1.trace("w",change_dropdown1)
    v2.trace("w",change_dropdown2)

    img=Image.open("C:\\Users\\Brij\\OneDrive\\Desktop\\Folders\\PSC_Project\\microphone.jfif")
    img=img.resize((50,50), Image.ANTIALIAS)
    img=ImageTk.PhotoImage(img)
    btn=tk.Button(mw3,text='Say Now!',image=img,compound=LEFT,command=speech_work)
    btn.place(x=300,y=220)
    
    quit=tk.Button(mw3,text="Quit",command=mw3.destroy,bg='red',font=5)
    quit.place(x=325,y=550)

    mw3.mainloop()
