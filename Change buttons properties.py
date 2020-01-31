#;==========================================
#; Title:  Change buttons properties
#; Author: @AyemunHossain
#;==========================================



import tkinter as tk

def action():
    print("Action !!!")



def create_button(row=1,column=1):
    # create a tons of empty buttons
    buttons = [[tk.Button() for j in range(column)] for i in range(row)]

    # Add details to the buttons and pack them
    for i in range(row):
        for j in range(column):
            buttons[i][j] = tk.Button(root, text="B", bg="brown", fg="white", bd=2, width=10, command=action)
            buttons[i][j].grid(row=i, column=j, sticky='news', padx=2, pady=2)


    #Here changes Button property after creation
    x = 0
    y =0
    while(x<row):
        y=0
        while(y<column):
            buttons[x][x].configure(text="C", bg="black", fg="white", bd=2, width=10)
            y+=1
        x += 1;


root = tk.Tk()
create_button(10,10)   #numbers of row and column
root.mainloop()

#the main intention behind this code: you can create tons of button in complex stucture like matrix structure
#and then you can change then like you want