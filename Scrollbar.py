#;==========================================
#; Title:  Tkinter Scrollbar
#; Author: @AyemunHossain
#;==========================================


from tkinter import *

root = Tk()
root.geometry('400x400')

frame1 = Frame(root)
frame1.pack(side=TOP, anchor=NW)

scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=Y)

listbox = Listbox(frame1, yscrollcommand=scrollbar.set, width=50, height=20, bg="brown",fg="white")
listbox.pack()
for i in range(500):
    listbox.insert(END, f"Item no {i}")

scrollbar.config(command=listbox.yview)


root.mainloop()