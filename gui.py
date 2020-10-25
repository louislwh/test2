# -*- coding: utf-8 -*-
"""
Created on Mon May 18 17:25:56 2020

@author: liwaiho
"""

from tkinter import *
import time

class Clock:
    def __init__(self,root):
        self.time1 = ''
        self.time2 = time.strftime('%H:%M:%S')
        self.mFrame = Frame(root)
        self.mFrame.configure(background='pale green')
        self.mFrame.pack(side=BOTTOM,anchor='w')
        self.watch = Label(self.mFrame, text=self.time2, font=('times',18,'bold'),background='pale green')
        self.watch.pack()
        self.changeLabel() #first call it manually
    def changeLabel(self): 
        self.time2 = time.strftime('%H:%M:%S')
        self.watch.configure(text=self.time2)
        self.mFrame.after(200, self.changeLabel) #it'll call itself continuously

class Menu_bar:
    def __init__(self,inp):
        self.inp = inp
        filemenu = Menu(inp)
        inp.config(menu=filemenu)
                
        menu1 = Menu(filemenu)
        menu1.add_command(label='new',command=self.new_window, accelerator='Ctrl-n')
        menu1.add_command(label='open')
        menu1.add_command(label='save')
        menu1.add_separator()
        menu1.add_command(label='exit',command=self.quit_window, accelerator='Crtl + t')
                
        menu2 = Menu(filemenu)
        menu2.add_command(label='copy')
        menu2.add_command(label='delete')    
                
        filemenu.add_cascade(label='file',menu=menu1)
        filemenu.add_cascade(label='edit',menu=menu2)
        
        inp.bind('<Control-t>',self.quit_window)
        inp.bind('<Control-n>',self.new_window)

    def quit_window(self,event='Control-t'):
        self.inp.destroy()
        print('exit') #debug message
    
    def new_window(self,event='Control-n'):
        exec(open("untitled2.py").read())
        print('new window') #debug message



root = Tk()
root.title('My tkinter GUI')
root.geometry('800x600')
root.configure(background='pale green')
label1 = Label(root,text='Hello , Tkinter!\r\n', background='orange').pack(anchor='center')

m = Menu_bar(root)

c = Clock(root)
e=Entry(root)
e.pack()
frame = Frame(root,width=60,height=10)
frame.pack()

bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )

redbutton = Button(frame, width=20,height=10, text="Red", fg="red")
redbutton.pack( side = LEFT)

greenbutton = Button(frame,width=20,height=10, text="Brown", fg="brown")
greenbutton.pack( side = LEFT )

bluebutton = Button(frame,width=20,height=10, text="Blue", fg="blue")
bluebutton.pack( side = LEFT )

blackbutton = Button(bottomframe, text="Exit", fg="black", command=root.destroy)
blackbutton.pack( side = BOTTOM)

root.mainloop()
