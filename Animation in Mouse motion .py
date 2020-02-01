#;====================================================
#; Title:  Animation in Mouse Motion
#; Author: @AyemunHossain
#;====================================================


import tkinter as tk
root = tk.Tk()

def animate(event):
    position = f"x = {event.x} y = {event.y}"
    print(f"{str(event.type)}, Event {position}")


    if str(event.type) is "Enter":
        canvus.config(bg="red")
    elif str(event.type) is "Motion":
        canvus.config(bg="green")
    elif str(event.type) is "ButtonRelease":
        canvus.config(bg="red")
    elif str(event.type) is "Leave":
        canvus.config(bg="gray")



canvus = tk.Canvas(root,width= 500,height=400,bg="gray")
canvus.pack(anchor = "nw")


canvus.bind("<B1-Motion>",lambda event:animate(event))
canvus.bind("<ButtonRelease-1>",lambda event:animate(event))
canvus.bind("<Enter>",lambda event:animate(event))
canvus.bind("<Leave>",lambda event:animate(event))


root.mainloop()