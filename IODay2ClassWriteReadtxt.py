from Tkinter import *
import ttk
import arcpy
import os
import string
from arcpy import env



files = []

class Scripts:
    
    def __init__(self, root):
        root.title("Python Script Browser")
        root.geometry("900x850")
        root.resizable(width=False, height=False)

        style = ttk.Style()
        style.configure("TButton", font="Serif", padding="15")

##        S = Scrollbar(root)
##        T = Text(root, height=150, width=150)
##        S.pack(Side=RIGHT, fill=y)
##        T.pack(side=LEFT, fill=y)
        
        
    def getScripts(self, root):
        
        env.workspace = "C:\ArcGIS_Scripts"
        ws = env.workspace
        pythonFiles = []
        for scrpt in os.listdir(ws):
            pythonFiles.append(scrpt)

        for (num, fn) in enumerate(pythonFiles):
            print (num + 1, str(fn)) 
            write_file = open("C:\ArcGIS_Scripts\TxtScrpts\scrpts.txt","w")
            pf = str(pythonFiles)
            write_file.write(pf + "\n")

        write_file.close()
    getScripts(root, files)  

root=Tk()


pyscripts = Scripts(root)
root.mainloop()