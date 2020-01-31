import tkinter as tk
window = tk.Tk()

window.title('App')

label1 = tk.Label(window,text="Hello World")
label1.pack(pady=20)

window.geometry("300x200+10+20")
window.mainloop()
