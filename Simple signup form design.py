#;==========================================
#; Title:  Simple Signup form
#; Author: @AyemunHossain
#;==========================================



from tkinter import *
def register():
    print("Successfully Registered")



root =Tk()
root.title("Rokto Cai")
frame=Frame(root)
frame.pack()

label1=Label(frame,text="First Name : ",fg="black")
label2=Label(frame,text="Last Name : ",fg="black")
label3=Label(frame,text="Phone Number : ",fg="black")
label4=Label(frame,text="Email : ",fg="black")
label5=Label(frame,text="Password : ",fg="black")

entry1=Entry(frame)
entry2=Entry(frame)
entry3=Entry(frame)
entry4=Entry(frame)
entry5=Entry(frame)


label1.grid(row=0,column=0,sticky=E)
label2.grid(row=1,column=0,sticky=E)
label3.grid(row=2,column=0,sticky=E)
label4.grid(row=3,column=0,sticky=E)
label5.grid(row=4,column=0,sticky=E)

entry1.grid(row=0,column=1)
entry2.grid(row=1,column=1)
entry3.grid(row=2,column=1)
entry4.grid(row=3,column=1)
entry5.grid(row=4,column=1)

check=Checkbutton(frame,text="I Agreed with all teams and condition",)
check.grid(row=5,columnspan=2)

button1=Button(frame,text="Sign up",bg="green",command=register)
button1.grid(column=10)

root.mainloop()
