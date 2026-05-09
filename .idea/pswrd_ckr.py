import random
import string
import tkinter as tk


root = tk.Tk(screenName= None, baseName= None, className= 'Tk', useTk= 1)
root.title('Password Cracker')


lsbx = tk.Listbox(root)
lsbx.pack()

lbl = tk.Label(text = '')
lbl.pack()
lbl2 = tk.Label(text = '')
lbl2.pack()

x = 0
used = []
usr_pswrd = str(input("Input user password between 8 and 12 charecters long: "))
while len(usr_pswrd)  > 12 or len(usr_pswrd) < 8 :
   usr_pswrd = str(input("Input user password between 8 and 12 charecters long: "))


while( x != usr_pswrd) :
  x = ''.join(random.choices(string.printable, k= len(usr_pswrd)))
  if x in used :
    continue
  lsbx.see(tk.END)
  used.append(x)
  lsbx.insert(tk.END, x)
  lbl.config(text=len(used))
  root.update()
   
else : 
 lbl2.config(text= x)
 lbl.config(text=len(used))



root.mainloop()