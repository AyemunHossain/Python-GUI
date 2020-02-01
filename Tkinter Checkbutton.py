import tkinter as tk


def get_chebutton(value):
    if value.get() == 1:
        print("Checked")
    else:
        print("Not Checked")

#.............Window and frame initializing...............
root=tk.Tk()
root.title(string='LOGIN PAGE')
root.geometry('550x180')
frame1=tk.Frame(root,height=10,width=550)
frame1.pack(side=tk.TOP)
frame1.pack_propagate(0)



label1=tk.Label(frame1,text='Email/Phone')
label2=tk.Label(frame1,text='Password')
label1.grid(row=0,column=1,sticky=tk.E)
label2.grid(row=1,column=1,sticky=tk.E)

entry1=tk.Entry(frame1)
entry2=tk.Entry(frame1)
entry1.grid(row=0,column=2)
entry2.grid(row=1,column=2)



#..............>>> Checkbutton <<<..............

check=tk.IntVar()

check_button=tk.Checkbutton(frame1,text='KEEP ME LOGGED IN',variable=check)
check_button.grid(row=3,column=1,rowspan=3,pady=2)

log=tk.Button(frame1,text='Login',command=lambda :get_chebutton(check) )
log.grid(row=5,column=5)



root.mainloop()