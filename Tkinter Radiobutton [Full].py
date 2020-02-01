# ;==========================================
# ; Title:  Login form in tkinter
# ; Author: @AyemunHossain
# ;==========================================

import tkinter as tk
from tkinter import messagebox


# Required Function
def check_info(r_val):
    if r_val.get() == 1:
        print("You are Male")
    elif r_val.get() == 2:
        print("You are Female")
    r_val.set(0)
    return


class LoginPage(tk.Tk):
    def __init__(self, root, *args, **kwargs):
        root.title(string='LOGIN PAGE')

        # Required variable)
        r_val = tk.IntVar()

        # Initializing frame
        frame1 = tk.Frame(root, height=400, width=400)
        frame1.pack()
        frame1.pack_propagate(0)
        label1 = tk.Label(frame1, text='Gender')
        label1.pack()

        # RadioButton
        r_buton1 = tk.Radiobutton(frame1, text="Male", value=1, variable=r_val)
        r_buton2 = tk.Radiobutton(frame1, text="Femake", value=2, variable=r_val)
        r_buton1.pack()
        r_buton2.pack()

        button1 = tk.Button(frame1, text='Check', width=10, bg="brown",fg="white", command=lambda: check_info(r_val))
        button1.pack()


root = tk.Tk()
root.geometry('550x180')

a = LoginPage(root)

root.mainloop()