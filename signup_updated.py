#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
# coding: utf-8

# In[3]:


from tkinter import *
import tkinter as tk
ans=""
def main():
    def get1(*args):
        global ans
        name = v1.get()
        ans=name
        #print(name)
    def save():
        global ans
        if(not ".jpg" in ans):
            ans+=".jpg"
        #print(ans)
    def fsnq():
        global ans
        if(not ".jpg" in ans):
            ans+=".jpg"
        mw1.destroy()
        #print(type(ans))
        #return ans
    mw1 = tk.Tk()
    mw1.title("Sorry! You are not found...")
    mw1.configure(background='aquamarine2')
    mw1.geometry("500x200")
    v1 = StringVar()
    e = tk.Entry(mw1,textvariable=v1,bg='lightblue',bd=4,font=10)
    l1 = tk.Label(mw1,bg='aquamarine2',text = "Enter Your Name :- ",font=10)
    l1.place(x=40,y=40)
    e.place(x=220,y=40)
    btn=tk.Button(mw1,text="Save",command=save,bg='green',font=5)
    btn.place(x=150,y=105)
    quit=tk.Button(mw1,text="Quit",command=mw1.destroy,bg='red',font=5)
    quit.place(x=300,y=105)
    snq=tk.Button(mw1,text="Save&Quit",command=fsnq,bg='salmon1',font=5)
    snq.place(x=200,y=150)
    v1.trace_add("write", get1)
    mw1.mainloop()
    #print(str(ans)+" ok")
    return ans
    
if __name__=="__main__":
    s=main()
    #print(str(s)+" main")

