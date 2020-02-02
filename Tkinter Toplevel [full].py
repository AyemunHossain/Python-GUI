#;==========================================
#; Title:  Tkinter Toplevel [full]
#; Author: @AyemunHossain
#;==========================================


import tkinter as tk

def box():

    top = tk.Toplevel()
    top.title("This is a Toplevel Widget")

    msg = tk.Message(top, text="And this is a message for you ")
    msg.pack()

    button = tk.Button(top, text="Ok", command=top.destroy,width=10)
    button.pack(pady=10,padx=10)

    top.tkraise()

root = tk.Tk()
root.geometry('500x500')
msg = tk.Label(root, text="Welcome to Hackerbook")
msg.pack()

button = tk.Button(root, text="See Toplevel", command=box)
button.pack()


root.mainloop()

