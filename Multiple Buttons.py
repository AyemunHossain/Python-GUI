#;==========================================
#; Title:  Tkinter Multiple Buttons
#; Author: @AyemunHossain
#;==========================================

from tkinter import *
root=Tk()
topFrame=Frame(root)
topFrame.pack()
bottomFrame=Frame(root)
bottomFrame.pack(side=BOTTOM)

button1= Button(topFrame,text="Follow",fg="red")
button2= Button(topFrame,text="Unfollow",fg="green")
button3= Button(bottomFrame,text="Connect",fg="blue")
button4= Button(bottomFrame,text="Disconnect",fg="black")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=RIGHT)


root.mainloop()