#;==========================================
#; Title:  Tkinter Load image
#; Author: @AyemunHossain
#;==========================================

import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Image")


image1 = ImageTk.PhotoImage(Image.open('Hacker.jpg'))
label = tk.Label(root, image=image1).pack()

root.mainloop()
