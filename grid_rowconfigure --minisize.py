#;==========================================
#; Title:  Grid Rowconfigurtion --minisize
#; Author: @AyemunHossain
#;==========================================



import tkinter as tk


#Decleare required function
def action():
    print("Action !!!")


root = tk.Tk()


#minisize : set the minimum size for any row or column
root.grid_rowconfigure(0,minsize=150)
root.grid_columnconfigure(1,minsize=150)
#see the changes in row 0 and column 1



row = 10
column = 5
buttons = [[tk.Button() for j in range(column)] for i in range(row)]

for i in range(row):
    for j in range(column):
        buttons[i][j] = tk.Button(root,text="B",bg="brown",fg="white",bd=2,width = 10,command=action)
        buttons[i][j].grid(row = i , column = j , sticky = 'news',padx=2,pady=2)


root.mainloop()


#Note: if you dont' use sticky = 'news' then you may find no changes 