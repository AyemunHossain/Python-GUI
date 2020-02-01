#;==========================================
#; Title:  Tkinter Listbox
#; Author: @AyemunHossain
#;==========================================

from tkinter import *

root = Tk()
frame1 = Frame(root)
frame1.pack(side=BOTTOM)


def delete_fun(listbox1):
    count =0
    for item in listbox1.curselection():
        item = item-count
        count+=1
        listbox1.delete(item)

    return



def order(listbox2, listbox1):
    [listbox2.insert(END,listbox1.get(item)) for item in listbox1.curselection()]
    return


listbox1 = Listbox(root, activestyle='dotbox', selectbackground='black', selectborderwidth=2,height=15,selectmode=MULTIPLE)
listbox1.pack()

# activestyle = selection style
# selectbackground  = selected items background
# selectmode = SINGLE, MULTIPLE, EXTENDED


listbox1.insert(END, "Polaw")

for item in ['Bread', 'Rice', 'Egg', 'Chicken', 'Beep','Drinks','Cheese','Pasta','Yogurt','Milk']:
    listbox1.insert(END, item)

b1 = Button(root, text="Delete", bg="brown", width=12, command=lambda: delete_fun(listbox1)).pack()
b2 = Button(root, text="Add To Cart", width=15, command=lambda: order(listbox2, listbox1)).pack()

listbox2 = Listbox(root, selectmode=SINGLE)
listbox2.pack()

root.mainloop()