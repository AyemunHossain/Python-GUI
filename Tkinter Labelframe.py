#;======================================================
#; Title:  set Bloodgroup with labelframe and optionmenu
#; Author: @AyemunHossain
#;======================================================

import tkinter as tk

root = tk.Tk()

group = tk.LabelFrame(root,height=40,width=80, text="Group")
group.pack(padx=10, pady=10)
group.pack_propagate(0)


blood_groups= ['A+','A-','B+','B-','Ab+','Ab-','O+','O-']
user_group = tk.StringVar()

op = tk.OptionMenu(group,user_group,*blood_groups)
op.pack()

button1 = tk.Button(text='See Group',width=10,bg='brown',fg='white',
                    command= lambda : [print(user_group.get()) if user_group.get() != '' else print("Select First")])
button1.pack()

root.mainloop()