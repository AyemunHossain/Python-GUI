#;==========================================
#; Title:  Tkinter Detect Mouse click
#; Author: @AyemunHossain
#;==========================================


import tkinter as tk
root = tk.Tk()


def action(event):
    position = f"x = {event.x} y = {event.y}"
    print(f"{str(event.type)}, Event {position}")

canvus = tk.Canvas(root,width= 500,height=400,bg="gray")
canvus.pack(anchor = "nw")

canvus.bind("<Button-1>",action)
canvus.bind("<Double-Button-1>",action)
canvus.bind("<ButtonRelease-1>",action)


root.mainloop()