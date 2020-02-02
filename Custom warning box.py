#;==========================================
#; Title:  Custom Warning box
#; Author: @AyemunHossain
#;==========================================

import tkinter as tk

def box():

    top = tk.Toplevel()
    top.title("Error")
    top.geometry('150x150')
    msg = tk.Message(top, text="Worng Input")
    msg.pack()

    button = tk.Button(top, text="Yes", width=15,bg='brown',fg='white',command=top.destroy)
    button.pack(side=tk.LEFT,pady=10,padx=15)

    top.tkraise()

root = tk.Tk()
root.geometry('500x500')

label = tk.Label(root, text="Welcome\nPlease login to continue")
label.pack(pady=20)

frame1 = tk.Frame(root)
frame1.pack()

label1=tk.Label(frame1,text='Email/Phone')
label2=tk.Label(frame1,text='Password')
label1.grid(row=0,column=1,sticky=tk.E)
label2.grid(row=1,column=1,sticky=tk.E)


entry1=tk.Entry(frame1)
entry2=tk.Entry(frame1)
entry1.grid(row=0,column=2)
entry2.grid(row=1,column=2)

button = tk.Button(frame1, text="Login",width=10, command=box)
button.grid(row=3,column=3)



root.mainloop()

