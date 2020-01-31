#create simple lebel 
'''from tkinter import *
root=Tk()
thelabel= Label(root,text="Hello World")
thelabel.pack()
root.mainloop()'''


#CREATE simple button 
'''
from tkinter import *
root=Tk()
topFrame=Frame(root)
topFrame.pack()
bottomFrame=Frame(root)
bottomFrame.pack(side=BOTTOM)

button1= Button(topFrame,text="Follow",fg="red")
button2= Button(topFrame,text="Unfollow",fg="green")
button3= Button(bottomFrame,text="Connect",fg="blue")
button4= Button(bottomFrame,text="Disconnect",fg="black")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=RIGHT)


root.mainloop()'''

#Dynamic lebel 

'''
from tkinter import *
root=Tk()
label1= Label(root,text="Hello World",bg="red",fg="black")
label1.pack(side=LEFT, fill=Y)
label2= Label(root,text="Bye World",bg="red",fg="black")
label2.pack(side=BOTTOM, fill=X)
label3= Label(root,text="Bye World",bg="red",fg="black")
label3.pack(side=RIGHT, fill=Y)
label3= Label(root,text="Bye World",bg="red",fg="black")
label3.pack(side=TOP, fill=X)


root.mainloop()'''


#let's know how gui screen grid works : 
'''from tkinter import *
root=Tk()

label1 = Label(root, text="Name : ")
label2 = Label(root, text="Password : ")
entry_1 = Entry(root)
entry_2 = Entry(root)

label1.grid(row=0, sticky=E)
label2.grid(row=1, sticky=E)

entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)

c=Checkbutton(root,text="Keep me logged in")
c.grid(columnspan=2)

root.mainloop()'''



    
'''#call any funciton by clicking button
def print_Qute():
    print("Everything Here is illusion")
    
from tkinter import *

root= Tk()
root.title("Ayemun Hossain Ashik")

frame=Frame(root)
frame.pack()


button1= Button(root, text="Click Me", command=print_Qute,width=50)
button1.pack(fill=X,side=TOP)

button2= Button(root, text="Exit", command=exit,fg="black",bg="red")
button2.pack(side=RIGHT)
root.mainloop()'''


'''def newdef(event):
      print("Hell !!! yeah there is that event")

from tkinter import *
root = Tk()
root.title("New App")
frame=Frame(root)
frame.pack()


button1=Button(frame,text="<Click Here>",bg="black",fg="white")
button1.bind("<Button-1>",newdef)
button1.grid(row=0,column=1)

root.mainloop()'''


'''
#pass the main window in a class as an instance of that class : 

from tkinter import *

def printMessage():
      print("OWO !!! It's works :) ")



class new:
  def __init__(self,master):
    frame=Frame(master)
    frame.pack()
    self.printButton=Button(frame,text="Click ME",command=printMessage)
    self.printButton.pack(side=LEFT)
    
    self.quitButton=Button(frame,text="Exit",command=frame.quit)
    self.quitButton.pack(side=RIGHT)
  
  
  
root=Tk()

n=new(root)

root.mainloop()
'''


#let's create a drop down manu in gui : 
'''
root = Tk()
menubar = Menu(root)
root.config(menu=menubar)     #it will configure the manu

fileMenu = Menu(menubar)

fileMenu.add_command(label="Open",command=action)
fileMenu.add_command(label="Save",command=action)
fileMenu.add_command(label="Save as",command=action)
fileMenu.add_separator()
fileMenu.add_command(label="Exit",command=root.quit)


menubar.add_cascade(label="File",menu=filemenu)
'''

'''
def action():
      print("Acton !!!")
      
from tkinter import *

root = Tk()
root.title("New Manu")
menubar = Menu(root)    #main menubar 
root.config(menu=menubar)     #here you have to give menu=your menu bar name


fileMenu = Menu(menubar,tearoff=0)  #sub menu 
menubar.add_cascade(label="File",menu=fileMenu) #attached sub menu to the menu 

fileMenu.add_command(label="Open",command=action)
fileMenu.add_command(label="Save",command=action)
fileMenu.add_command(label="Save as",command=action)
fileMenu.add_separator() 
fileMenu.add_command(label="Exit",command=root.quit)

#create the edit menu 
editMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=editMenu)

editMenu.add_command(label="Edit", command=action)
editMenu.add_command(label="Cut", command=action)
editMenu.add_command(label="Copy", command=action)
editMenu.add_command(label="Paste", command=action)


#create the help menu 
helpMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=helpMenu)

helpMenu.add_command(label="About",command=action)
helpMenu.add_command(label="Help",command=action)


root.mainloop()
'''
'''
#creating a tool bar 
def p():
      print("Ashik")
      
from tkinter import *

root=Tk()

frame1 = Frame(root,bg="green")

button1 = Button(frame1,text="Home",command=p)
button1.pack(side=LEFT,padx=2, pady=5)
button2 = Button(frame1,text="Profile",command=p)
button2.pack(side=LEFT,padx=2, pady=5)
button3 = Button(frame1,text="Message",command=p)
button3.pack(side=LEFT,padx=2, pady=5)
button4 = Button(frame1,text="Find Friends",command=p)
button4.pack(side=LEFT,padx=2, pady=5)
button5 = Button(frame1,text="See Request",command=p)
button5.pack(side=LEFT,padx=2, pady=5)
button6 = Button(frame1,text="Chat",command=p)
button6.pack(side=LEFT,padx=2, pady=5)

frame1.pack(side=TOP,fill=X)

root.mainloop()
'''
#Create a tons of button list 

'''def action():
    print("Action !!!")

import tkinter as tk


root = tk.Tk()


row = 10 
column = 5 
#creater a tons of empty buttons
buttons = [[tk.Button() for j in range(column)] for i in range(row)]

#Add details to the buttons and pack them  
for i in range(row):
    for j in range(column):
        buttons[i][j] = tk.Button(root,text="B",bg="brown",fg="white",bd=2,width = 10,command=action)
        buttons[i][j].grid(row = i , column = j , sticky = 'news',padx=2,pady=2)


#changes after creation 
buttons[0][1] = tk.Button(root,text="C",bg="brown",fg="white",bd=2,width = 10,command=action)
buttons[0][1].grid(row = 0 , column = 1 , sticky = 'news',padx=2,pady=2)




root.mainloop()'''


'''def p():
      print("Ashik")
      
from tkinter import *

root=Tk()

frame1 = Frame(root,bg="green",borderwidth=2 )

button1 = Button(frame1,text="Home", command=p)
button1.pack(side=LEFT,padx=2, pady=5)
button2 = Button(frame1,text="Profile",command=p)
button2.pack(side=LEFT,padx=2, pady=5)
button3 = Button(frame1,text="Message",command=p)
button3.pack(side=LEFT,padx=2, pady=5)
button4 = Button(frame1,text="Find Friends",command=p)
button4.pack(side=LEFT,padx=2, pady=5)
button5 = Button(frame1,text="See Request",command=p)
button5.pack(side=LEFT,padx=2, pady=5)
button6 = Button(frame1,text="Chat",command=p)
button6.pack(side=LEFT,padx=2, pady=5)

frame1.pack(side=TOP,fill=X)

root.mainloop()
'''

'''def new():
      print("Win or leave it")
      
      
#toolbar and footer       
from tkinter import *

root=Tk()
root.title("New App")
root.geometry('400x600+100+100')
frame1 = Frame(root,borderwidth=10)
frame2 = Frame(root,borderwidth=100)


button1 = Button(frame1,text="Home", command=new)
button1.pack(side=LEFT,padx=4)
button2 = Button(frame1,text="Profile",command=new)
button2.pack(side=LEFT)
button3 = Button(frame1,text="Message",command=new)
button3.pack(side=LEFT)
button4 = Button(frame1,text="Find Friends",command=new)
button4.pack(side=LEFT)
button5 = Button(frame1,text="See Request",command=new)
button5.pack(side=LEFT)
button6 = Button(frame1,text="Chat",command=new)
button6.pack(side=LEFT)


label1= Label(frame2,text="This is an footer view for the frame",bg="red",bd=1,relief=SUNKEN,anchor=W,pady=10,padx=20)
label1.pack(side = BOTTOM,fill=X)
frame1.pack(side= TOP )
frame2.pack(side= BOTTOM,fill=X)



root.mainloop()'''

'''def new():
      print("Win or leave it")
      
      
#toolbar and footer       
from tkinter import *

root=Tk()
root.title("New App")
root.geometry('600x800+100+100')
frame1 = Frame(root,borderwidth=10)
frame2 = Frame(root,borderwidth=100)

button1 = Button(frame1,text="Home", command=new)
button1.pack(side=LEFT,padx=4)
button2 = Button(frame1,text="Profile",command=new)
button2.pack(side=LEFT)
button3 = Button(frame1,text="Message",command=new)
button3.pack(side=LEFT)
button4 = Button(frame1,text="Find Friends",command=new)
button4.pack(side=LEFT)
button5 = Button(frame1,text="See Request",command=new)
button5.pack(side=LEFT)
button6 = Button(frame1,text="Chat",command=new)
button6.pack(side=LEFT)


label1= Label(frame2,text="This is an footer view for the frame",bg="red",bd=1,relief=SUNKEN,pady=10,padx=20)
label1.pack(side = BOTTOM,fill=X,expand=TRUE)


frame1.pack(side= TOP )
frame2.pack(side= BOTTOM,fill=BOTH,expand=TRUE)




root.mainloop()'''



#message box 




#set default entry value : 
'''
    image1 = ImageTk.PhotoImage(Image.open('tout-member-login_0.webp'))
    im_label = Label(FF1,image=image1).pack()'''



#image file with tkinter : 

'''
#with tkinter module you can only work wit png image
from tkinter import *
root= Tk()

image1 = PhotoImage(file="rokto_home.png")

label = Label(root,image=image1,width=400,height=400,bg="#a7d6dc").pack()

root.mainloop()
'''

#But if you want to work with any kind of picture fomate then you will need to work with PIL 

'''from tkinter import *
from PIL import Image,ImageTk
root=Tk()

image1=Image.open("angel.jpg")
label = Label(root,image=image1,width=400,height=400,bg="#a7d6dc").pack()


root.mainloop()'''

'''def new():
      print("i love you")
      
      
#gui slider 
from tkinter import *
root=Tk()

new=IntVar
myslider = Scale(root,from_=1971,variable=new,to=2019,resolution=1,orient= HORIZONTAL,label="Age",tickinterval=5,length=400,sliderlength=25).pack()


#resolution = means the value of sinle part of the scale 
#highlightbackground = is the side border of the main scale body 
#troughcolor = background of the actual scale body 
#fg = is the font color of the scale 
#activebackground = is the color of scale button when you put curser on it 
#sliderlength = is the lengeth of slider of the scale 
#length  = the length of the scale body 
#tickinterval = is the interval of the vlue that is shown in donw of the scale

root.mainloop()
'''

'''
from tkinter import *

root=Tk()
def delete_fun(listbox):
      listbox.delete(ACTIVE)
      return



def get_fun(listbox):
      if len(listbox.curselection()) is 0:
            print("level e nai")
      else:
            pass 
            #need to learn class based gui then you can implement this shit 
            #label1 = Label(root,text=f"{listbox.get(listbox.curselection())}",bg="brown",fg="white").pack()
            
def order(listbox2,index):
      item=listbox2.get(index)
      listbox2.insert(END,item)
      return
      
listbox1 = Listbox(root,activestyle='dotbox',selectbackground='black',selectborderwidth=2,selectmode=MULTIPLE)
listbox1.pack()
#activestyle = when you select any item of the box
#selectbackground  = selected items background
#selectmode = SINGLE, MULTIPLE, EXTENDED


listbox1.insert(END,"Polaw")

for item in ['Chicken Polaw','Beep Polaw','Egg Polaw','Chicken Danduri','Kacchi Biriyani']:
      listbox1.insert(END,item)


b1= Button(root,text="Delete",bg="brown",width=12,command= lambda: delete_fun(listbox1)).pack()
b2= Button(root,text="Get",bg="brown",width=12,command=lambda :get_fun(listbox1)).pack()
b3= Button(root,text="Add To Cart",width=15,command=lambda:order(listbox2,listbox1.curselection())).pack()

listbox2 = Listbox(root,selectmode=SINGLE)
listbox2.pack()



root.mainloop()
'''

'''
#Create a Scrollbar 
from tkinter import *

root=Tk()
root.geometry('500x500+100+100')

scrollbar1 = Scrollbar(root)
scrollbar1.pack(side =RIGHT,fill= Y)
frame1 = Frame(root, width = 500, height = 500,bg='brown')      
frame1.pack(side=TOP,anchor = NW)




scrollbar = Scrollbar(frame1)
scrollbar.pack(side =RIGHT,fill= Y)

listbox = Listbox(frame1, yscrollcommand = scrollbar.set,width=50,height=20,bg="brown")
listbox.pack()
for i in range(500):
      listbox.insert(END,f"Item no {i}")
     

scrollbar.config(command= listbox.yview)
scrollbar1.config()





root.mainloop()
'''

'''
#all kind of event in tkinter 
import tkinter as tk 
root = tk.Tk()
key=[]
def down(event):
    if not event.keysym in key:
        print(f"{event.keysym} is pressed")
        try:
            key.append(event.keysym)
        except:
            return
    return
def up(event):
    if event.keysym in key:
        print(f"{event.keysym} is released")
        try:
            key.remove(event.keysym)
        except:
            return
        return
    
def action(event):
    position = f"x = {event.x} y = {event.y}"
    print(f"{str(event.type)}, Event {position}")

canvus = tk.Canvas(root,width= 500,height=400,bg="gray")
canvus.pack(anchor = "nw")

canvus.bind("<Button-1>",action)
canvus.bind("<Double-Button-1>",action)
canvus.bind("<ButtonRelease-1>",action)
canvus.bind("<B1-Motion>",action)
canvus.bind("<Enter>",action)
canvus.bind("<Leave>",action)
canvus.bind("<Shift-Up>",action)
canvus.bind_all("<KeyPress>",down) #with out binding all i can't detected a keybord key 
canvus.bind_all("<KeyRelease>",up) #with out binding all i can't detected a keybord key
canvus.bind("<Keyboard>",key)


root.mainloop()
'''
#Make someting like status bar : *(here you can find how to change any widget after creation) 

'''import time
def status():
      #making an animation on status bar 
      
      label.configure(fg="red")
      st.set("Wait")
      label.update() 
      time.sleep(1)
      label.configure(fg="red")
      st.set("Wait...")
      label.update() 
      time.sleep(1)
      st.set("Wait.....")
      label.configure(fg="red")
      
      button1.configure(bg="white",fg="red",state=tk.DISABLED)
      label.update() 
      button1.update()
      time.sleep(2)
      st.set("Ready")
      label.configure(fg="green")
      button1.configure(bg=ori,state=tk.NORMAL,fg="white")


import tkinter as tk

root = tk.Tk()
root.geometry("500x500")


button1 = tk.Button(root,text= "Upload File",width=10,command=status,bg="brown",fg="white")
button1.pack()
ori=button1.cget("bg") #You can get any of widget vaule 



st=tk.StringVar()
st.set("*Ready")

label= tk.Label(root,textvariable=st,relief=tk.SUNKEN,bd=1,anchor=tk.W,padx=30,fg="green")
label.pack(side=tk.BOTTOM,fill=tk.X)




root.mainloop()'''



#>>>>>>>>>>>>Object Oriented TKinter<<<<<<<<<

#Basic base opp class
'''

import tkinter as tk


class seaofBTCapp(tk.Tk):
    def __init__(self,*args,**kwargs):

        #here we initialize the TK
        tk.Tk.__init__(self,*args,**kwargs)

        #container(A orginised frame) will hold the frame that will use for the window
        container=tk.Frame(self)
        container.pack(side="top",fill="both",expand=True)
        container.grid_rowconfigure(0,weight=1)     #configure the row
        container.grid_columnconfigure(0, weight=1)   #configure the column

        self.frames={}

        frame = StartPage(container,self)

        self.frames[StartPage] = frame

        frame.grid(row=0,column=0,sticky="news")

        self.show_frame(StartPage)

    def show_frame(self,cont):
        frame=self.frames[cont]
        frame.tkraise()




class StartPage(tk.Frame):
    def __init__(self,parent,container):
        tk.Frame.__init__(self,parent)
        label1 = tk.Label(self,text = "This is and orginised tkinter app you can build awesome things")
        label1.pack(pady=10,padx=5)


app=seaofBTCapp()
app.mainloop()


'''



#Multiple page OPP
'''
#>>>>>>>>>>>>Object Oriented TKinter<<<<<<<<<


import tkinter as tk


class seaofBTCapp(tk.Tk):
    def __init__(self,*args,**kwargs):

        #here we initialize the TK
        tk.Tk.__init__(self,*args,**kwargs)

        #container(A orginised frame) will hold the frame that will use for the window
        container=tk.Frame(self)
        container.pack(side="top",fill="both",expand=True)
        container.grid_rowconfigure(0,weight=1)     #configure the row
        container.grid_columnconfigure(0, weight=1)   #configure the column

        self.frames={}


        for F in (PageHome,PageProfile,PageTimeline,PageAbout,PageLike,PageSecurity):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="news")

        self.show_frame(PageHome)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class PageHome(tk.Frame):
    def __init__(self,parent,container):

        tk.Frame.__init__(self,parent)
        label1 = tk.Label(self,text = "Welcome to our social media !!!! \n Wish you have FUN! :) ")
        label1.pack(pady=10,padx=5)

        button1 = tk.Button(self, text="Profile", width=10, command=
                            lambda:container.show_frame(PageProfile))
        button1.pack()

        button2 = tk.Button(self, text="Timeline", width=10, command=
                            lambda:container.show_frame(PageTimeline))
        button2.pack()

        button3 = tk.Button(self, text="Likes", width=10, command=
                            lambda:container.show_frame(PageLike))
        button3.pack()

        button4 = tk.Button(self, text="Security", width=10, command=
                            lambda:container.show_frame(PageSecurity))
        button4.pack()

        button5 = tk.Button(self, text="About", width=10, command=
                            lambda:container.show_frame(PageAbout))
        button5.pack()


class PageProfile(tk.Frame):

    def __init__(self,parent,container):

        tk.Frame.__init__(self,parent)
        label1 = tk.Label(self, text="Your Profile !!!!")
        label1.pack(pady=10, padx=5)

        button1 = tk.Button(self, text="About", width=10, command=
                            lambda:container.show_frame(PageAbout))
        button1.pack()

        button2 = tk.Button(self, text="Timeline", width=10, command=
                            lambda:container.show_frame(PageTimeline))
        button2.pack()

        button3 = tk.Button(self, text="Likes", width=10, command=
                            lambda:container.show_frame(PageLike))
        button3.pack()

        button4 = tk.Button(self, text="Security", width=10, command=
                            lambda:container.show_frame(PageSecurity))
        button4.pack()

        button5 = tk.Button(self, text="Home", width=10, command=
                            lambda:container.show_frame(PageHome))
        button5.pack()



class PageAbout(tk.Frame):

    def __init__(self,parent,container):

        tk.Frame.__init__(self,parent)
        label1 = tk.Label(self, text="About Yourself :) ")
        label1.pack(pady=10, padx=5)

        button1 = tk.Button(self, text="Profile", width=10, command=
                            lambda:container.show_frame(PageProfile))
        button1.pack()

        button2 = tk.Button(self, text="Timeline", width=10, command=
                            lambda:container.show_frame(PageTimeline))
        button2.pack()

        button3 = tk.Button(self, text="Likes", width=10, command=
                            lambda:container.show_frame(PageLike))
        button3.pack()

        button4 = tk.Button(self, text="Security", width=10, command=
                            lambda:container.show_frame(PageSecurity))
        button4.pack()

        button5 = tk.Button(self, text="Home", width=10, command=
                            lambda:container.show_frame(PageHome))
        button5.pack()

class PageTimeline(tk.Frame):

    def __init__(self,parent,container):

        tk.Frame.__init__(self,parent)
        label1 = tk.Label(self, text="Your recents Post : ")
        label1.pack(pady=10, padx=5)

        button1 = tk.Button(self, text="Profile", width=10, command=
                            lambda:container.show_frame(PageProfile))
        button1.pack()

        button2 = tk.Button(self, text="About", width=10, command=
                            lambda:container.show_frame(PageAbout))
        button2.pack()

        button3 = tk.Button(self, text="Likes", width=10, command=
                            lambda:container.show_frame(PageLike))
        button3.pack()

        button4 = tk.Button(self, text="Security", width=10, command=
                            lambda:container.show_frame(PageSecurity))
        button4.pack()

        button5 = tk.Button(self, text="Home", width=10, command=
                            lambda:container.show_frame(PageHome))
        button5.pack()


class PageLike(tk.Frame):

    def __init__(self,parent,container):

        tk.Frame.__init__(self,parent)
        label1 = tk.Label(self, text="Things you have liked :) ")
        label1.pack(pady=10, padx=5)

        button1 = tk.Button(self, text="Profile", width=10, command=
                            lambda:container.show_frame(PageProfile))
        button1.pack()

        button2 = tk.Button(self, text="Timeline", width=10, command=
                            lambda:container.show_frame(PageTimeline))
        button2.pack()

        button3 = tk.Button(self, text="About", width=10, command=
                            lambda:container.show_frame(PageAbout))
        button3.pack()

        button4 = tk.Button(self, text="Security", width=10, command=
                            lambda:container.show_frame(PageSecurity))
        button4.pack()

        button5 = tk.Button(self, text="Home", width=10, command=
                            lambda:container.show_frame(PageHome))
        button5.pack()


class PageSecurity(tk.Frame):

    def __init__(self,parent,container):

        tk.Frame.__init__(self,parent)
        label1 = tk.Label(self, text="Security Issue")
        label1.pack(pady=10, padx=5)

        button1 = tk.Button(self, text="Profile", width=10, command=
                            lambda:container.show_frame(PageProfile))
        button1.pack()

        button2 = tk.Button(self, text="Timeline", width=10, command=
                            lambda:container.show_frame(PageTimeline))
        button2.pack()

        button3 = tk.Button(self, text="Likes", width=10, command=
                            lambda:container.show_frame(PageLike))
        button3.pack()

        button4 = tk.Button(self, text="About", width=10, command=
                            lambda:container.show_frame(PageAbout))
        button4.pack()

        button5 = tk.Button(self, text="Home", width=10, command=
                            lambda: container.show_frame(PageHome))
        button5.pack()


app=seaofBTCapp()
app.mainloop()



'''





'''class MyApp:                                                                          # defines class
    def __init__(self, main):                                                         # this function is run once an instance of the class is created

        self.main_frame = main                                                        # creates a new frame called 'main_frame' and places it in the parent frame 'main'
        tk.Grid.rowconfigure(self.main_frame, 0, weight=1)                            # not sure what this does
        tk.Grid.columnconfigure(self.main_frame, 0, weight=1)                         # not sure what this does

        self.checkbutton_frame = tk.Frame(self.main_frame)                            # creates a new frame called 'checkbutton_frame' and places it in the 'main_frame'
        self.checkbutton_frame.grid(row=0, column=1)

        self.button_frame = tk.Frame(self.main_frame)                                 # creates a new frame called 'button_frame' and places it in the 'main_frame'
        self.button_frame.grid(row=0, column=0, sticky='nsew')                        # not sure what this does
        tk.Grid.rowconfigure(self.button_frame, 7, weight=1)                          # not sure what this does
        tk.Grid.columnconfigure(self.button_frame, 0, weight=1)                       # not sure what this does

        self.grid = tk.Frame(self.button_frame)                                       # creates a new frame called 'grid' and places it in the 'button_frame'
        self.grid.grid(sticky='nsew', column=0, row=7, columnspan=2)                  # not sure what this does

        self.createbuttongrid()                                                       # calls the 'createbuttongrid' function
        self.createcheckbuttons()                                                     # calls the 'createcheckbuttons' function

    def createcheckbuttons(self):
        for row in range(6):
            checkbutton = tk.Checkbutton(self.checkbutton_frame, text='Checkbutton')  # creates checkbuttons
            checkbutton.grid(row=row, column=0)                                       # places checkbuttons on rows/columns

    def createbuttongrid(self):
        for row in range(8):
            for column in range(12):
                button = tk.Button(self.button_frame, text='Button')                  # creates buttons
                button.grid(row=row, column=column, sticky='nsew')                    # places buttons

        for row in range(8):
            tk.Grid.rowconfigure(self.button_frame, row, weight=1)                    # not sure what this does
        for column in range(12):
            tk.Grid.columnconfigure(self.button_frame, column, weight=1)              # not sure what this does

if __name__ == "__main__":
    import tkinter as tk                                              # import statement
    root = tk.Tk()                                                    # initializes the Tk window
    MyApp(main=root)                                                  # tells the class that it should use this instance of the Tk() window. I can create multiple windows that interact separately by creating multiple tk.Tk()'s'''