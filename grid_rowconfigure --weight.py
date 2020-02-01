
#;==========================================
#; Title:  Grid Rowconfigurtion --minisize
#; Author: @AyemunHossain
#;==========================================

import tkinter as tk

#Decleare required function
def action():
    print("Action !!!")


root = tk.Tk()

#weight : weight for particular row or column when window size is shrinking
root.grid_rowconfigure(2, weight=10)
root.grid_columnconfigure(3, weight=2)
#see the changes in row 2and column 3
row = 10
column = 5
buttons = [[tk.Button() for j in range(column)] for i in range(row)]


for i in range(row):
    for j in range(column):
        buttons[i][j] = tk.Button(root, text="B", bg="brown", fg="white",bd=2, width = 10, command=action)
        buttons[i][j].grid(row = i , column = j, sticky = 'news', padx=2, pady=2)




root.mainloop()


#Shrink the window make it bigger and see the magic
#Note if you don't user sticky = 'news' then you may don't find any changes/ unwanted changes