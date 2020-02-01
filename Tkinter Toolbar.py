#;==========================================
#; Title:  Tkinter toolbar
#; Author: @AyemunHossain
#;==========================================



from tkinter import *


def p():
    print("You Clicked")
    
root = Tk()
root.geometry('400x400')

frame1 = Frame(root, bg="gray")
frame1.pack(side=TOP, fill=X)

button1 = Button(frame1, text="Home", command=p)
button1.pack(side=LEFT, padx=2, pady=5)
button2 = Button(frame1, text="Profile", command=p)
button2.pack(side=LEFT, padx=2, pady=5)
button3 = Button(frame1, text="Message", command=p)
button3.pack(side=LEFT, padx=2, pady=5)
button4 = Button(frame1, text="Find Friends", command=p)
button4.pack(side=LEFT, padx=2, pady=5)
button5 = Button(frame1, text="See Request", command=p)
button5.pack(side=LEFT, padx=2, pady=5)
button6 = Button(frame1, text="Chat", command=p)
button6.pack(side=LEFT, padx=2, pady=5)



root.mainloop()