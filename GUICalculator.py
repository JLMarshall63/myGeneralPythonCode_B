from Tkinter import *
import ttk

class Calculator:
    calc_value = 0.0

    div_trigger = False
    mult_trigger = False
    sum_trigger = False
    sub_trigger = False

    def button_press(self, value):
        #number = 0.0
        entry_val = self.number_entry.get()
        entry_val += value
        self.number_entry.delete(0, "end")
        self.number_entry.insert(0, entry_val)

    def clear_button_press(self, value):
        self.number_entry.delete(0, "end")    

    def isfloat(self, str_val):
        try:
            float(str_val)
            return True
        except ValueError:
            return False

    def math_button_press(self, value):
        if self.isfloat(str(self.number_entry.get())):
            self.div_trigger = False
            self.mult_trigger = False
            self.sum_trigger = False
            self.sub_trigger = False
            
            self.calc_value = float(self.entry_value.get())

            if value == "/":
                print("/ Pressed")
                self.div_trigger = True

            elif value == "*":
                print("* Pressed")
                self.mult_trigger = True

            elif value == "+":
                print("+ Pressed")
                self.sum_trigger = True

            else:
                print("- Pressed")
                self.sub_trigger = True

            self.number_entry.delete(0, "end")

    def equal_button_press(self, value):
        if self.sub_trigger or self.sum_trigger or self.mult_trigger or self.div_trigger:
            if self.sum_trigger:
                solution = self.calc_value + float(self.entry_value.get())
            elif self.sub_trigger:
                solution = self.calc_value - float(self.entry_value.get())
            elif self.mult_trigger:
                solution = self.calc_value * float(self.entry_value.get())
            else:
                solution = self.calc_value / float(self.entry_value.get())
        
            print(self.calc_value, " ", float(self.entry_value.get()), " ", solution)

            self.number_entry.delete(0, "end")
            self.number_entry.insert(0, solution)
                
    def __init__(self, root):
        self.entry_value = StringVar(root,value="")

        root.title("Calculator")
        root.geometry("600x250")
        root.resizable(width=False, height=False)

        style = ttk.Style()
        style.configure("TButton", font="Serif 15", padding=10)
        style.configure("TEntry", font=("Serif",20), padding=10)

        self.number_entry = ttk.Entry(root, textvariable=self.entry_value, width=50)
        self.number_entry.grid(row=0, columnspan=4)
        #1st row
        self.bttn1 = ttk.Button(root, text="1", command=lambda: self.button_press('1')).grid(row=1, column=0)
        self.bttn2 = ttk.Button(root, text="2", command=lambda: self.button_press('2')).grid(row=1, column=1)
        self.bttn3 = ttk.Button(root, text="3", command=lambda: self.button_press('3')).grid(row=1, column=2)
        self.bttn_sum = ttk.Button(root, text="+", command=lambda: self.math_button_press('+')).grid(row=1, column=3)
        #2nd row
        self.bttn4 = ttk.Button(root, text="4", command=lambda: self.button_press('4')).grid(row=2, column=0)
        self.bttn5 = ttk.Button(root, text="5", command=lambda: self.button_press('5')).grid(row=2, column=1)
        self.bttn6 = ttk.Button(root, text="6", command=lambda: self.button_press('6')).grid(row=2, column=2)
        self.bttn_sub = ttk.Button(root, text="-", command=lambda: self.math_button_press('-')).grid(row=2, column=3)        
        #3rd row
        self.bttn7 = ttk.Button(root, text="7", command=lambda: self.button_press('7')).grid(row=3, column=0)
        self.bttn8 = ttk.Button(root, text="8", command=lambda: self.button_press('8')).grid(row=3, column=1)
        self.bttn9 = ttk.Button(root, text="9", command=lambda: self.button_press('9')).grid(row=3, column=2)
        self.bttn_div = ttk.Button(root, text="/", command=lambda: self.math_button_press('/')).grid(row=3, column=3)
        #4th row
        self.bttn0 = ttk.Button(root, text="0", command=lambda: self.button_press('0')).grid(row=4, column=0)
        self.bttn_equal = ttk.Button(root, text="=", command=lambda: self.equal_button_press('=')).grid(row=4, column=1)
        self.bttn_clear = ttk.Button(root, text="AC", command=lambda: self.clear_button_press('AC')).grid(row=4, column=2)
        self.bttn_mult = ttk.Button(root, text="*", command=lambda: self.math_button_press('*')).grid(row=4, column=3)
        

root=Tk()
calc = Calculator(root)

root.mainloop()

                

                
        