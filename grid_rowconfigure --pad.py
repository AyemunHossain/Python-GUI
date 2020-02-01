#;==========================================
#; Title:  Grid Rowconfigurtion --pad
#; Author: @AyemunHossain
#;==========================================



import tkinter as tk

#Decleare required function
def action():
    print("Action !!!")


root = tk.Tk()

#pad : use for adding pad in required row and column
root.grid_rowconfigure(0,pad=50)
root.grid_columnconfigure(3,pad=50)
#see the changes in row 0 and column 3

row = 10
column = 5
buttons = [[tk.Button() for j in range(column)] for i in range(row)]


for i in range(row):
    for j in range(column):
        buttons[i][j] = tk.Button(root,text="B",bg="brown",fg="white",bd=2,width = 10,command=action)
        buttons[i][j].grid(row = i , column = j , sticky = 'news',padx=2,pady=2)




root.mainloop()