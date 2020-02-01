#;====================================================
#; Title:  Tkinter Mouse & keyboard all kinds of event
#; Author: @AyemunHossain
#;====================================================


import tkinter as tk
root = tk.Tk()
key=[]
def down(event):
    if not event.keysym in key:
        print(f"{event.keysym} is pressed")
        try:
            key.append(event.keysym)
        except:
            return
    return
def up(event):
    if event.keysym in key:
        print(f"{event.keysym} is released")
        try:
            key.remove(event.keysym)
        except:
            return
        return

def action(event):
    position = f"x = {event.x} y = {event.y}"
    print(f"{str(event.type)}, Event {position}")

canvus = tk.Canvas(root,width= 500,height=400,bg="gray")
canvus.pack(anchor = "nw")

canvus.bind("<Button-1>",action)
canvus.bind("<Double-Button-1>",action)
canvus.bind("<ButtonRelease-1>",action)
canvus.bind("<B1-Motion>",action)
canvus.bind("<Enter>",action)
canvus.bind("<Leave>",action)
canvus.bind("<Shift-Up>",action)
canvus.bind_all("<KeyPress>",down)
canvus.bind_all("<KeyRelease>",up)
canvus.bind("<Keyboard>",key)


root.mainloop()