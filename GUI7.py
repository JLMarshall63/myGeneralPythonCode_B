from Tkinter import *
root = Tk()

def printName():
	print "My fist name is John."
	

button_1 = Button(root, text="Print Name", command=printName)
button_1.pack()


def printName2(event):
	print "My last name is Marshall."
	

button_2 = Button(root, text="Print Name2")
button_2.bind("<Button-1>", printName2)
button_2.pack()


def leftClick(event):
    print ("left")

def middleClick(event):
    print("middle")

def rightClick(event):
    print("right")

frame = Frame(root, width="300", height="500")
frame.bind("<Button-1>", leftClick)
frame.bind("<Button-2>", middleClick)
frame.bind("<Button-3>", rightClick)
frame.pack()


root.mainloop()    