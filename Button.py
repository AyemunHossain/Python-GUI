#;==========================================
#; Title:  Tkinter Button
#; Author: @AyemunHossain
#;==========================================


import tkinter as tk

def action():
    print("Action!!!")


window = tk.Tk()

window.title('App')

label1 = tk.Label(text="Hello World")
label1.pack(pady=20)

button1 = tk.Button(text="Click Me",width=10,bg='brown',fg='white',command=action)
button1.pack()

window.geometry("300x200+10+20")
window.mainloop()
