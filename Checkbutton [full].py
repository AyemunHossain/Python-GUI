import tkinter as tk
from tkinter import messagebox

def check_info(e1,e2,ch):
    if(e1.get() =='' or e2.get() == ''):
        messagebox.showerror("You need to fill everything")
    elif ch.get() == 0:
        messagebox.showwarning("Fill the checkbox")
    else:
        messagebox.showinfo("Registration Successful :)")
        e1.set('')
        e2.set('')
        ch.set(0)
    return

class LoginPage(tk.Tk):
    def __init__(self,root,*args,**kwargs):
        root.title(string='LOGIN PAGE')

        #Required variable
        e1 = tk.StringVar()
        e2 = tk.StringVar()
        ch = tk.IntVar()

        frame1 = tk.Frame(root,height=400,width=400)
        frame1.pack()

        label1 = tk.Label(frame1, text='Name')
        label2 = tk.Label(frame1, text='Password')
        label1.grid(row=4, column=0, sticky=tk.E)
        label2.grid(row=5, column=0, sticky=tk.E)

        entry1 = tk.Entry(frame1,textvariable=e1)
        entry2 = tk.Entry(frame1,textvariable=e2)
        entry1.grid(row=4, column=1)
        entry2.grid(row=5, column=1)

        chk = tk.Checkbutton(frame1, text='KEEP ME LOGGED IN',variable=ch)
        chk.grid(row=6, column=1)

        btn = tk.Button(frame1, text='SUBMIT',command=lambda :check_info(e1,e2,ch))
        btn.grid(row=7, column=1)


root = tk.Tk()
root.geometry('550x180')

a = LoginPage(root)

root.mainloop()