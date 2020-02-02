#;==========================================
#; Title:  Tkinter PanedWindow [all].py
#; Author: @AyemunHossain
#;==========================================

import tkinter as tk


def pan():

    frame1=tk.Frame(root)
    frame1.pack(anchor='w')

    frame1.grid_rowconfigure(0,minsize=400)
    frame1.grid_columnconfigure(0,minsize=600)

    pan1 = tk.PanedWindow(frame1,height=400,width=600,bg="black")
    pan1.grid(row=0,column=0)
    pan1.grid_propagate(0)

    label1 = tk.Label(pan1,text="Afghanistan \nAlbania \nAlgeria \nAndorra \nAngola \nAntigua \nArgentina")
    pan1.add(label1,width=150)
    label1.grid_propagate(0)
    pan1.paneconfig(label1, minsize=100)

    label2 = tk.Label(pan1, text="Bangladesh \nIndia \nPakistan \nNepal \nBhutan \nJapna")
    pan1.add(label2,width=150)
    label2.grid_propagate(0)
    pan1.paneconfig(label2, minsize=100)

    pan2 = tk.PanedWindow(pan1,height=200,width=300,bg="brown",orient=tk.VERTICAL)
    pan1.add(pan2)
    pan2.grid_propagate(0)

    label3= tk.Label(pan2,text="We all loves to walking on beach \nAnd enjoy the sunset")
    pan2.add(label3,height=200)
    pan2.paneconfig(label3, minsize=100)

    pan2.grid_propagate()
    label4 = tk.Label(pan2, text="We all hates to waiting on Airports \nAnd watching freking people")
    pan2.add(label4,height=200)
    pan2.paneconfig(label4, minsize=100)

root = tk.Tk()
pan()
root.mainloop()
