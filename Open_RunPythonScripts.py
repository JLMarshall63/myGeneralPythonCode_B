from Tkinter import *
import ttk
from tkFileDialog import askopenfilename

def callback():
    abc = askopenfilename()
    #print abc
    execfile(abc)

a = Button(text='Run Python File', command=callback)
a.pack()

#root = Tk()
mainloop()
    