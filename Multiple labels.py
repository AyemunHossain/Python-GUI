#;==========================================
#; Title:  Tkinter Multiple Labels
#; Author: @AyemunHossain
#;==========================================

from tkinter import *


root=Tk()
root.geometry('200x300')
label1= Label(root,text="Left",bg="brown",fg="black")
label1.pack(side=LEFT, fill=Y)

label2= Label(root,text="Right",bg="brown",fg="black")
label2.pack(side=RIGHT, fill=Y)

label3= Label(root,text="Bottom",bg="red",fg="black")
label3.pack(side=BOTTOM, fill=X)

label4= Label(root,text="Top",bg="black",fg="white")
label4.pack(side=TOP, fill=X)


root.mainloop()