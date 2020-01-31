import tkinter as tk
from tkinter import ttk
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style

style.use('ggplot')

f = Figure(figsize=(5, 5), dpi=100)
a = f.add_subplot(111)

def animate(i):
    data = open("e1.txt","r").read()
    split_data = data.split('\n')
    x=[]
    y=[]
    for l in split_data:
        try:
            b, c = l.split(',')
            x.append(int(b))
            y.append(int(c))
        except:
            pass

    a.clear()
    a.plot(x,y)
    a.set_xlabel("X Labels")
    a.set_ylabel("Y Labels")


class Major(tk.Tk):

    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        tk.Tk.geometry(self, '800x600')
        tk.Tk.title(self,"Bitcoin Exchange")
        tk.Tk.iconbitmap(self,"picandicon//bitcoin.ico")

        containter = tk.Frame(self)
        containter.pack(side="top",fill="both",expand=True)
        containter.grid_rowconfigure(0,weight=1)
        containter.grid_columnconfigure(0, weight=1)

        self.frames={}

        for F in (HomePage,PageOne,PageTwo,GraphPage):
            frame = F(self,containter)
            self.frames[F] = frame
            frame.grid(row=0,column=0,sticky='news')

        self.show_frames(HomePage)

    def show_frames(self,cont):
        frame = self.frames[cont]
        frame.tkraise()



class HomePage(tk.Frame):
    def __init__ (self,parent_class,parent_frame):
        tk.Frame.__init__(self,parent_frame)

        label1 = tk.Label(self,text="It's Your Home Page!!!")
        label1.pack(pady=30)

        button1= tk.Button(self,text="Page One",width=10,bg='brown',
                           fg='white',command=lambda:parent_class.show_frames(PageOne))
        button1.pack()

        button2= tk.Button(self,text="Page Two",width=10,bg='brown',
                           fg='white',command=lambda:parent_class.show_frames(PageTwo))
        button2.pack()

        button3 = tk.Button(self, text="Graph Page", width=10, bg='brown',
                            fg='white', command=lambda: parent_class.show_frames(GraphPage))
        button3.pack()

class PageOne(tk.Frame):
    def __init__(self,parent_class,parent_frame):
        tk.Frame.__init__(self,parent_frame)

        label1 = tk.Label(self, text="It's Your Page One!!!")
        label1.pack(pady=30)

        button1 = tk.Button(self, text="Home Page", width=10, bg='brown',
                            fg='white', command=lambda: parent_class.show_frames(HomePage))
        button1.pack()

        button2 = tk.Button(self, text="Page Two", width=10, bg='brown',
                            fg='white', command=lambda: parent_class.show_frames(PageTwo))
        button2.pack()

        button3 = tk.Button(self, text="Grpah Page", width=10, bg='brown',
                            fg='white', command=lambda: parent_class.show_frames(GraphPage))
        button3.pack()




class PageTwo(tk.Frame):
    def __init__(self,parent_class,parent_frame):
        tk.Frame.__init__(self,parent_frame)

        label1 = tk.Label(self, text="It's Your Page Two!!!")
        label1.pack(pady=30)

        button1 = tk.Button(self, text="Home Page", width=10, bg='brown',
                            fg='white', command=lambda: parent_class.show_frames(HomePage))
        button1.pack()

        button2 = tk.Button(self, text="Page One", width=10, bg='brown',
                            fg='white', command=lambda: parent_class.show_frames(PageOne))
        button2.pack()

        button3 = tk.Button(self, text="Graph Page", width=10, bg='brown',
                            fg='white', command=lambda: parent_class.show_frames(GraphPage))
        button3.pack()


class GraphPage(tk.Frame):
    def __init__(self,parent_class,parent_frame):
        tk.Frame.__init__(self,parent_frame)

        label1 = tk.Label(self, text="Graph Page!!!")
        label1.pack(pady=30)
        button1 = tk.Button(self, text="Home Page", width=10, bg='brown',
                            fg='white', command=lambda: parent_class.show_frames(HomePage))
        button1.pack()

        button2 = tk.Button(self, text="Page One", width=10, bg='brown',
                            fg='white', command=lambda: parent_class.show_frames(PageOne))
        button2.pack()

        button3 = tk.Button(self, text="Page Two", width=10, bg='brown',
                            fg='white', command=lambda: parent_class.show_frames(PageTwo))
        button3.pack()
        canvas = FigureCanvasTkAgg(f,self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP,fill = tk.BOTH,expand= True)


app=Major()
ani = animation.FuncAnimation(f,animate)
app.mainloop()
