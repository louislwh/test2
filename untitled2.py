# -*- coding: utf-8 -*-
"""
Created on Mon May 18 17:25:56 2020

@author: liwaiho
"""

from tkinter import *
import time

expression=""

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

class Calculator:      
   def clear():
       global expression 
       expression = "" 
       equation.set("") 
       
   def press(num): 
        # point out the global expression variable 
        global expression 
      
        # concatenation of string 
        expression = expression + str(num) 
      
        # update the expression by using set method 
        equation.set(expression) 
        
   def equalpress(): 
        # Try and except statement is used 
        # for handling the errors like zero 
        # division error etc. 
      
        # Put that code inside the try block 
        # which may generate the error 
        try: 
            global expression 
      
            # eval function evaluate the expression 
            # and str function convert the result 
            # into string 
            total = str(eval(expression)) 
      
            equation.set(total) 
      
            # initialze the expression variable 
            # by empty string 
            expression = "" 
      
        # if error is generate then handle 
        # by the except block 
        except: 
            equation.set(" error ") 
            expression = ""
        
 
    
    
try:
    root = Tk()
    root.title('My tkinter GUI')
    root.geometry('800x600')
    root.configure(background='pale green')
    label1 = Label(root,text='Hello , Tkinter!\r\n', background='orange').pack(anchor='center')
    m = Menu_bar(root)
    c = Clock(root)
    
    frame = Frame(root)
    frame.pack()
    equation = StringVar()  
    expression_field = Entry(frame, textvariable=equation) 
    expression_field.grid(columnspan=4, ipadx=70) 
    equation.set('enter your expression')

    

    button1 = Button(frame, text=' 1 ', fg='black', bg='red', 
                     command=lambda: Calculator.press(1), height=1, width=7) 
    button1.grid(row=2, column=0) 
  
    button2 = Button(frame, text=' 2 ', fg='black', bg='red', 
                     command=lambda: Calculator.press(2), height=1, width=7) 
    button2.grid(row=2, column=1) 
  
    button3 = Button(frame, text=' 3 ', fg='black', bg='red', 
                     command=lambda: Calculator.press(3), height=1, width=7) 
    button3.grid(row=2, column=2) 
  
    button4 = Button(frame, text=' 4 ', fg='black', bg='red', 
                     command=lambda: Calculator.press(4), height=1, width=7) 
    button4.grid(row=3, column=0) 
  
    button5 = Button(frame, text=' 5 ', fg='black', bg='red', 
                     command=lambda: Calculator.press(5), height=1, width=7) 
    button5.grid(row=3, column=1) 
  
    button6 = Button(frame, text=' 6 ', fg='black', bg='red', 
                     command=lambda: Calculator.press(6), height=1, width=7) 
    button6.grid(row=3, column=2) 
  
    button7 = Button(frame, text=' 7 ', fg='black', bg='red', 
                     command=lambda: Calculator.press(7), height=1, width=7) 
    button7.grid(row=4, column=0) 
  
    button8 = Button(frame, text=' 8 ', fg='black', bg='red', 
                     command=lambda: Calculator.press(8), height=1, width=7) 
    button8.grid(row=4, column=1) 
  
    button9 = Button(frame, text=' 9 ', fg='black', bg='red', 
                     command=lambda: Calculator.press(9), height=1, width=7) 
    button9.grid(row=4, column=2) 
  
    button0 = Button(frame, text=' 0 ', fg='black', bg='red', 
                     command=lambda: Calculator.press(0), height=1, width=7) 
    button0.grid(row=5, column=0) 
  
    plus = Button(frame, text=' + ', fg='black', bg='red', 
                  command=lambda: Calculator.press("+"), height=1, width=7) 
    plus.grid(row=2, column=3) 
  
    minus = Button(frame, text=' - ', fg='black', bg='red', 
                   command=lambda: Calculator.press("-"), height=1, width=7) 
    minus.grid(row=3, column=3) 
  
    multiply = Button(frame, text=' * ', fg='black', bg='red', 
                      command=lambda: Calculator.press("*"), height=1, width=7) 
    multiply.grid(row=4, column=3) 
  
    divide = Button(frame, text=' / ', fg='black', bg='red', 
                    command=lambda: Calculator.press("/"), height=1, width=7) 
    divide.grid(row=5, column=3) 
  
    equal = Button(frame, text=' = ', fg='black', bg='red', 
                   command=Calculator.equalpress, height=1, width=7) 
    equal.grid(row=5, column=2) 
  
    clear = Button(frame, text='Clear', fg='black', bg='red', 
                   command=Calculator.clear, height=1, width=7) 
    clear.grid(row=5, column='1') 
  
    Decimal= Button(frame, text='.', fg='black', bg='red', 
                    command=lambda: Calculator.press('.'), height=1, width=7) 
    Decimal.grid(row=6, column=0) 

    
    
    # redbutton = Button(bottomframe, width=20,height=10, text="Red", fg="red")
    # redbutton.pack( side = LEFT)
    
    # greenbutton = Button(bottomframe,width=20,height=10, text="Brown", fg="brown")
    # greenbutton.pack( side = LEFT )
    
    # bluebutton = Button(bottomframeframe,width=20,height=10, text="Blue", fg="blue")
    # bluebutton.pack( side = LEFT )
    bottomframe = Frame(root)
    bottomframe.pack( side = BOTTOM )
    blackbutton = Button(bottomframe, text="Exit", fg="black", command=root.destroy)
    blackbutton.pack( side = BOTTOM)
except:
    print("something wrong")
    

root.mainloop()
