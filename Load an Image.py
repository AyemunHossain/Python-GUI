#;==========================================
#; Title:  Tkinter Load image
#; Author: @AyemunHossain
#;==========================================



from tkinter import *
root= Tk()

image1 = PhotoImage(file="Hacker.png")        #By tkinter PhotoImage module you can workwith .png only

label = Label(root,image=image1,bg="#a7d6dc").pack()

root.mainloop()


#So here's and hack you will find if you run this code with the appropriate image :
#Hack is : 
'''
  If you wanna add any jpg file with tkinter module then all you have to do is 
  convert your image with appropriate height and width then do it 
  and sing :
            I am begining feel like a Hacker good, Hacker good
            all my code are from front to the back nod, back nod
            now, who things their lengths are not long enough to Hack-box :) :))
            They said I Hack like Mr.Robot, so call me elliot.....
        
'''