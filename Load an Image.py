#;==========================================
#; Title:  Tkinter Load image
#; Author: @AyemunHossain
#;==========================================



from tkinter import *
root= Tk()

image1 = PhotoImage(file="logo.png")        #By tkinter PhotoImage module you can workwith .png only

label = Label(root,image=image1,width=400,height=400,bg="#a7d6dc").pack()

root.mainloop()
