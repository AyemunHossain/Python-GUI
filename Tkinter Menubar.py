#;==========================================
#; Title:  Tkinter MenuBar
#; Author: @AyemunHossain
#;==========================================

import tkinter as tk

root = tk.Tk()
root.geometry('400x400')
root.title("Menubar")
menubar = tk.Menu(root)
root.config(menu=menubar)

fileMenu = tk.Menu(menubar)
menubar.add_cascade(label="File",menu=fileMenu)

fileMenu.add_command(label="Open")
fileMenu.add_command(label="Save")
fileMenu.add_command(label="Save as")
fileMenu.add_separator()
fileMenu.add_command(label="Exit")


root.mainloop()