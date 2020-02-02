# ;==========================================
# ; Title:  Tkinter Optionmenu [full]
# ; Author: @AyemunHossain
# ;==========================================

import tkinter as tk
from tkinter import  messagebox
root = tk.Tk()



frame1 = tk.Frame(root)
frame1.pack(expand=tk.TRUE)

country_v= tk.StringVar()
country_v.set("Select One")

f = open("all_country.txt",'r')
data = f.read()
linedata= data.split('\n')

country_list = []
for line in linedata:
    country_list.append(line)
f.close()


label1 = tk.Label(frame1,text="Select Your Country: ",bg="#ada4a3")
label1.pack(side=tk.TOP)

country = tk.OptionMenu(frame1, country_v, *country_list)
country.pack()


button2 = tk.Button(frame1,text="My Country",width=10,bg='brown',fg='white',
                    command=lambda :[messagebox.showerror("Select First") if str(country_v.get()) == "Select One"
                                        else print(f"Your Country is {country_v.get()}")])
button2.pack()

root.mainloop()