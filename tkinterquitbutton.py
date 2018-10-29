#!/usr/bin/env python
import tkinter as tk
class Application(tk.Frame):
    def __init__(self,master=None):
        tk.Frame.__init__(self,master)
        self.grid(sticky=tk.N+tk.S+tk.E+tk.W)
        self.createWidgets()
    def createWidgets(self):
        top = self.winfo_toplevel()
        top.rowconfigure(0,weight=1)
        top.columnconfigure(0,weight=1)
        self.rowconfigure(0,weight=1)
        self.columnconfigure(0,weight=1)
        self.quitButton= tk.Button(self,name="quitButton",text='Quit',command=self.quit)
        self.quitButton.grid(row=0,column=0,sticky=tk.SW)#sticky=tk.N+tk.S+tk.E+tk.W


app = Application()
app.master.title('Python Quit Button Application')
app.master.geometry('1200x500+100+100')
app.mainloop()