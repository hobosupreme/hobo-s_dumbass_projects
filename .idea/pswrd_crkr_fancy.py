#imports
import random
import string
import tkinter as tk



#creates tk window
root = tk.Tk(screenName= None, baseName= None, className= 'Tk', useTk= 1)
root.title('Password Cracker')



#varibles
x = ''
y = ''
pswrd = []
pswrd_temp = ''
usr_pswrd = []



#fuction for entry wiget text
def clear(event):
    if pswrd_entry.get() == 'input pasword':
        pswrd_entry.delete(0, tk.END)
        pswrd_entry.config(fg='black')



#guess 
def chr_gs() :
  chr = ''.join(random.choices(string.printable, k= 1))
  return chr



#basiclly everything
def get_psw() :
 #random stuff i need
 pswrdy = False
 k = int(0)
 usr_pswrd = list(pswrd_entry.get())

 #checks password
 if len(usr_pswrd) < 8 or len(usr_pswrd) > 12:
    lbl3.config(text= 'no, fix')
    return
 
 #main guess loop
 while(pswrdy == False) : 
   #gets and inserts guess
   x = chr_gs()
   lsbxy.insert(tk.END, x)

   #checks if the guess is correct
   if(x != list(usr_pswrd)[k]) :
    continue
   #turns the corrrect guesses to a str and does tk stuff
   pswrd.append(x)
   pswrdz = ''.join(pswrd)
   lsbx.insert(tk.END, pswrdz)
   lsbx.see(tk.END)
   lsbxy.see(tk.END)
   root.update()

   #checks password
   if(pswrd == list(usr_pswrd)) :
    pswrdy = True

   #misc
   k += 1
   lbl2.config(text= k)
   root.update()

 #final updates
 lbl.config(text= pswrdz)
 lbl2.config(text= k)
 root.update()



#tk listbox stuff
lsbx = tk.Listbox(root)
lsbx.pack(side= 'left', fill= 'y',  expand= True)
lsbxy = tk.Listbox(root)
lsbxy.pack(side= 'left', fill= 'y', expand= True)

#tk label stuff
lbl = tk.Label(root, text = 'number of charecters in password')
lbl.pack(side= 'bottom', expand= True)
lbl2 = tk.Label(root, text = 'password')
lbl2.pack(side= 'bottom', expand= True)
lbl3 = tk.Label(root, text = '')
lbl3.pack(side= 'top', expand= True)

#entry wiget stuff
pswrd_entry = tk.Entry(root, fg='grey')
pswrd_entry.insert(0, 'input pasword')
pswrd_entry.bind("<FocusIn>", clear)
pswrd_entry.pack(side= 'right', expand= True)

#button
btn = tk.Button(root, text= 'start', command= get_psw)
btn.pack(side= 'bottom', expand= True)

  
root.mainloop()