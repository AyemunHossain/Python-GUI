
#;==========================================
#; Title:  Login form in tkinter
#; Author: @AyemunHossain
#;==========================================


import tkinter as tk


#............functions..............
def action():
    print ('Action !!!')
def p():
    pass


#.............Window and frame initializing...............
root=tk.Tk()
root.title(string='LOGIN PAGE')
root.geometry('550x180')
frame1=tk.Frame(root,height=40,width=550)
frame1.pack(side=tk.TOP)
frame1.pack_propagate(0)
frame2=tk.Frame(root,height=40,width=550)
frame2.pack(side=tk.TOP,fill=tk.X)
frame2.pack_propagate(0)
frame3=tk.Frame(root)
frame3.pack(side=tk.TOP,anchor='w',padx=50,expand=tk.TRUE)

#................Manubar................

#Main menubar
menubar = tk.Menu(frame1)
root.config(menu=menubar)

#Edit Menu
fileMenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=fileMenu)

fileMenu.add_command(label="Open", command=action)
fileMenu.add_command(label="Save", command=action)
fileMenu.add_command(label="Save as", command=action)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=root.quit)

#Edit Menu
editMenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=editMenu)

editMenu.add_command(label="Edit", command=action)
editMenu.add_command(label="Cut", command=action)
editMenu.add_command(label="Copy", command=action)
editMenu.add_command(label="Paste", command=action)

#Help Menu
helpMenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=helpMenu)
helpMenu.add_command(label="About", command=action)
helpMenu.add_command(label="Help", command=action)
helpMenu.add_command(label="Ask a Question", command=action)
helpMenu.add_command(label="See Frequenly asked question", command=action)
helpMenu.add_command(label="Send Feadback", command=action)


#...............toolbar..............
toolbar = tk.Frame(frame1, bg="grey")
button1 = tk.Button(frame1, text="Registration", command=p)
button1.pack(side=tk.LEFT, padx=2, pady=5)
button2 = tk.Button(frame1, text="Watch", command=p)
button2.pack(side=tk.LEFT, padx=2, pady=5)
button3 = tk.Button(frame1, text="People", command=p)
button3.pack(side=tk.LEFT, padx=2, pady=5)
button4 = tk.Button(frame1, text="Find Friends", command=p)
button4.pack(side=tk.LEFT, padx=2, pady=5)
button5 = tk.Button(frame1, text="Pages", command=p)
button5.pack(side=tk.LEFT, padx=2, pady=5)
button6 = tk.Button(frame1, text="Places", command=p)
button6.pack(side=tk.LEFT, padx=2, pady=5)
button7 = tk.Button(frame1, text="Games", command=p)
button7.pack(side=tk.LEFT, padx=2, pady=5)
button8 = tk.Button(frame1, text="Marketplace", command=p)
button8.pack(side=tk.LEFT, padx=2, pady=5)
button9 = tk.Button(frame1, text="Location", command=p)
button9.pack(side=tk.LEFT, padx=2, pady=5)


label=tk.Label(frame2,text='Hackerbook',fg='white',bg="brown")
label.pack(pady=10)

#..............Entery and labels............
label1=tk.Label(frame3,text='Email/Phone')
label2=tk.Label(frame3,text='Password')
label1.grid(row=7,column=1,sticky=tk.E)
label2.grid(row=8,column=1,sticky=tk.E)

entry1=tk.Entry(frame3)
entry2=tk.Entry(frame3)
entry1.grid(row=7,column=2)
entry2.grid(row=8,column=2)

#checkbutton
check_button=tk.Checkbutton(frame3,text='KEEP ME LOGGED IN')
check_button.grid(row=11,column=1,rowspan=3,pady=2)

log=tk.Button(frame3,text='Login')
log.grid(row=11,column=5)



root.mainloop()