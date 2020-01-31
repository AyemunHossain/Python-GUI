#;==========================================
#; Title:  OOP Concept with tkinter GUI
#; Author: @AyemunHossain
#;==========================================

import tkinter as tk


def printMessage():
    print("OWO !!! It's works :) ")


class MainPage(tk.Tk):
    def __init__(self, master):
        frame = tk.Frame(master)
        frame.pack()
        self.printButton = tk.Button(frame, text="Click ME",bg="red",fg="white",width=10, command=printMessage)
        self.printButton.pack(side=tk.LEFT,pady=20)

        self.quitButton = tk.Button(frame, text="Exit",bg="brown",fg="white",width=10, command=frame.quit)
        self.quitButton.pack(side=tk.RIGHT,padx=20)


root = tk.Tk()
root.geometry('400x400')
# pass the main window in a class as an instance of that class :)
n = MainPage(root)

root.mainloop()