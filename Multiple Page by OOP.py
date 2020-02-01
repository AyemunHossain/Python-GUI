#;=============================================================
#; Title:  Multiple page handeling in object oriented apporach
#; Author: @AyemunHossain
#;=============================================================

import tkinter as tk


class MainClass(tk.Tk):
    def __init__(self,*args,**kwargs):

#Initialize the TK
        tk.Tk.__init__(self,*args,**kwargs)

        container=tk.Frame(self)
        container.pack(side="top",fill="both",expand=True)
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0, weight=1)

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
        label1 = tk.Label(self,text = "Welcome \n Wish you have FUN! :) ")
        label1.pack(pady=50,padx=5)

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
        label1.pack(pady=50,padx=5)

        button1 = tk.Button(self, text="Home", width=10, command=
                            lambda:container.show_frame(PageHome))
        button1.pack()

        button2 = tk.Button(self, text="About", width=10, command=
                            lambda:container.show_frame(PageAbout))
        button2.pack()

        button3 = tk.Button(self, text="Timeline", width=10, command=
                            lambda:container.show_frame(PageTimeline))
        button3.pack()

        button4 = tk.Button(self, text="Likes", width=10, command=
                            lambda:container.show_frame(PageLike))
        button4.pack()

        button5 = tk.Button(self, text="Security", width=10, command=
                            lambda:container.show_frame(PageSecurity))
        button5.pack()



class PageAbout(tk.Frame):

    def __init__(self,parent,container):

        tk.Frame.__init__(self,parent)
        label1 = tk.Label(self, text="About Yourself :) ")
        label1.pack(pady=50,padx=5)

        button1 = tk.Button(self, text="Profile", width=10, command=
                            lambda:container.show_frame(PageProfile))
        button1.pack()

        button2 = tk.Button(self, text="Home", width=10, command=
                            lambda:container.show_frame(PageHome))
        button2.pack()

        button3 = tk.Button(self, text="Timeline", width=10, command=
                            lambda:container.show_frame(PageTimeline))
        button3.pack()

        button4 = tk.Button(self, text="Likes", width=10, command=
                            lambda:container.show_frame(PageLike))
        button4.pack()

        button5 = tk.Button(self, text="Security", width=10, command=
                            lambda:container.show_frame(PageSecurity))
        button5.pack()


class PageTimeline(tk.Frame):

    def __init__(self,parent,container):

        tk.Frame.__init__(self,parent)
        label1 = tk.Label(self, text="Your recent Posts : ")
        label1.pack(pady=50,padx=5)

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
        label1.pack(pady=50,padx=5)

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
        label1 = tk.Label(self, text="Security Issues Here")
        label1.pack(pady=50,padx=5)

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


app=MainClass()
app.mainloop()
