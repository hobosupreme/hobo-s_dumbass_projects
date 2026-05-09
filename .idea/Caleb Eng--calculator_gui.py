# imports the tkinter lib
import tkinter as tk

#function defenitions
def add() :
     global c
     a = int(entry1.get())
     b = int(entry2.get())
     c = a + b
     my_label.config(text=f"Result: {c}")
     # print(c)

def sub() :
     global c
     a = int(entry1.get())
     b = int(entry2.get())
     c = a - b
     my_label.config(text=f"Result: {c}")
     # print(c)

def mult() :
     global c
     a = int(entry1.get())
     b = int(entry2.get())
     c = a * b
     my_label.config(text=f"Result: {c}")
     
def div() :
     global c
     a = int(entry1.get())
     b = int(entry2.get())
     c = a / b
     # print(c)
     my_label.config(text=f"Result: {c}")

#initiates the window
root = tk.Tk(screenName=None,baseName=None, className='Tk',useTk=1)
root.title("Calculator")


#creates the labels and entries for the number inptus 
tk.Label(root, text="first number").grid(row=0, column=0)
tk.Label(root, text="second number").grid(row=1, column=0)
entry1 = tk.Entry(root)
entry2 = tk.Entry(root)
entry1.grid(row=0, column=4)
entry2.grid(row=1, column=4)

#adds oporator buttons 
tk.Button(root, text="+", command = add).grid(row = 4, sticky=tk.W)
tk.Button(root, text="-", command = sub).grid(row = 5, sticky=tk.W) 
tk.Button(root, text="*", command = mult).grid(row = 6, sticky=tk.W)
tk.Button(root, text="/", command = div).grid(row = 7, sticky=tk.W)

#displays the result
my_label = tk.Label(text = '')
my_label.grid(row=4, column=4)

#prevents the window from closing 
root.mainloop()