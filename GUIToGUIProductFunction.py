from Tkinter import *
import ttk

def get_product(event):
    num1 = int(num1Entry.get())
    num2 = int(num2Entry.get())
    prod = num1 * num2
    prodEntry.insert(0, prod)

root = Tk()

num1Entry = Entry(root)
num1Entry.pack(side=LEFT)

Label(root, text= " * ").pack(side=LEFT)

num2Entry = Entry(root)
num2Entry.pack(side=LEFT)

equalButton = Button(root,text="=")
equalButton.bind("<Button-1>", get_product)
equalButton.pack(side=LEFT)

prodEntry = Entry()
prodEntry.pack(side=LEFT)

root.mainloop()