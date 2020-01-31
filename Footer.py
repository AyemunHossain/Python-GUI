#;==========================================
#; Title:  Tkinter Footer
#; Author: @AyemunHossain
#;==========================================

def new():
    print("Win or leave it")


# toolbar and footer
from tkinter import *

root = Tk()
root.title("Desktop App")
root.geometry('400x600')


frame1 = Frame(root,borderwidth=10,bg="blue")
frame2 = Frame(root, borderwidth=100)
frame1.pack(side=TOP)
frame2.pack(side=BOTTOM, fill=X)

button1 = Button(frame1, text="Home", command=new)
button1.pack(side=LEFT)
button2 = Button(frame1, text="Profile", command=new)
button2.pack(side=LEFT)
button3 = Button(frame1, text="Message", command=new)
button3.pack(side=LEFT)
button4 = Button(frame1, text="Find Friends", command=new)
button4.pack(side=LEFT)
button5 = Button(frame1, text="See Request", command=new)
button5.pack(side=LEFT)
button6 = Button(frame1, text="Chat", command=new)
button6.pack(side=LEFT)

label1 = Label(frame2, text="This is an footer view for the frame", bg="brown",fg="white",
               bd=1, relief=SUNKEN, pady=10,padx=20)

label1.pack(side=BOTTOM, fill=X)


root.mainloop()