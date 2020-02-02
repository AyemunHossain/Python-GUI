#;==========================================
#; Title:  Tkinter Spinbox
#; Author: @AyemunHossain
#;==========================================

import tkinter as tk

root = tk.Tk()

def set_date():

    label= tk.Label(root,text='Select one :').pack()
    w_val = tk.IntVar()
    
    w = tk.Spinbox(root, from_=1, to=30, textvariable=w_val)
    w.pack()


    button2 = tk.Button(root,text="See", width=10,bg="brown",fg='white',
                        command=lambda : print(w_val.get()))
    button2.pack()

set_date()
root.mainloop()