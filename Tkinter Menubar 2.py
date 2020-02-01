#;==========================================
#; Title:  Tkinter MenuBar 2
#; Author: @AyemunHossain
#;==========================================



def action():
    print("Acton !!!")

def why():
    print("Why so serious man :) ")

import tkinter as tk

root = tk.Tk()
root.title("New Manu")
root.geometry('400x400')

menubar = tk.Menu(root)
root.config(menu=menubar)

#Created Edit Menu
fileMenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=fileMenu)

fileMenu.add_command(label="Open", command=action)
fileMenu.add_command(label="Save", command=action)
fileMenu.add_command(label="Save as", command=action)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=root.quit)

#Created Edit Menu
editMenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=editMenu)

editMenu.add_command(label="Edit", command=action)
editMenu.add_command(label="Cut", command=action)
editMenu.add_command(label="Copy", command=action)
editMenu.add_command(label="Paste", command=action)

#Created Help Menu
helpMenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=helpMenu)
helpMenu.add_command(label="About", command=action)
helpMenu.add_command(label="Help", command=action)
helpMenu.add_command(label="Ask a Question", command=action)
helpMenu.add_command(label="See Frequenly asked question", command=action)
helpMenu.add_command(label="Send Feadback", command=action)



label1 = tk.Label(text="Manubar",bg="red",fg="white",bd=10)
label1.pack(pady=20,fill=tk.X)

button1 = tk.Button(text="Click Me",width=10,bg='brown',fg='white',command=why)
button1.pack()




root.mainloop()