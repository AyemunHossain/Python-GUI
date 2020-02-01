#;=============================================================
#; Title:  Multiple page handeling in object oriented apporach
#; Author: @AyemunHossain
#;=============================================================

import tkinter as tk
import time



class FileUpload(tk.Tk):

    def __init__(self,root,*args,**kwargs):
        root.geometry('400x400')


        self.label1 = tk.Label(root,text="Upload Your profile picture:").pack(side=tk.TOP)
        self.button1 = tk.Button(root,text="Upload",width=10,bg="brown",fg="white",command=self.upload_file)
        self.button1.pack(pady=35)
        self.label2 = tk.Label(root,text="System Free",relief=tk.SUNKEN,bd=2,anchor=tk.W)
        self.label2.pack(side=tk.BOTTOM, fill=tk.X,padx=2)



    def upload_file(self):
        self.button1.configure(bg="white",state=tk.DISABLED)
        self.button1.update()
        self.label2.configure(text="File Uplading ....",fg="green")
        self.label2.update()
        time.sleep(1.1)
        self.label2.configure(text="Wait ....",fg="brown")
        self.label2.update()
        time.sleep(1.1)
        self.status()


    def status(self):
        self.label2.configure(text="File Uploaded :)",fg="green")
        self.label2.update()
        time.sleep(0.5)
        self.button1.configure(bg="brown", state=tk.NORMAL)
        self.button1.update()


root = tk.Tk()
file1 = FileUpload(root)
root.mainloop()