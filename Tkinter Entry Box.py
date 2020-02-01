#;==========================================
#; Title:  Tkinter Entry Box
#; Author: @AyemunHossain
#;==========================================


from tkinter import *
root=Tk()

label1 = Label(root, text="Name : ")
label2 = Label(root, text="Password : ")
entry_1 = Entry(root)
entry_2 = Entry(root)

label1.grid(row=0, sticky=E)
label2.grid(row=1, sticky=E)

entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)

c=Checkbutton(root,text="Keep me logged in")
c.grid(columnspan=2)

root.mainloop()