#;==========================================
#; Title:  Tkinter Scale
#; Author: @AyemunHossain
#;==========================================

from tkinter import *

root = Tk()

myslider = Scale(root, from_=1971, to=2019, resolution=1,
                 orient=HORIZONTAL, label="Age", tickinterval=5,
                 length=400, sliderlength=25)
myslider.pack()

button1 = Button(text="Watch the Value",width=15,bg="brown",
                 fg="white",bd=3,command=lambda :print(myslider.get()))
button1.pack(pady=20)



# resolution = Value of single part of the scale
# highlightbackground = Side border of the scale body
# troughcolor = Background of the actual scale body
# activebackground = Color of scale button when you press slider
# sliderlength = Lengeth of slider of the scale
# length  = Length of the scale body
# tickinterval = Interval in value of Scale

root.mainloop()