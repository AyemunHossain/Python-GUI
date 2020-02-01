#;==========================================
#; Title:  Tkinter Spinbox
#; Author: @AyemunHossain
#;==========================================



from tkinter import *

master = Tk()

w = Spinbox(master, from_=0, to=10)
w.pack()

button = Button(text="Click me",width=10)
button.pack()

mainloop()