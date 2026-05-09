import random
import string
import tkinter as tk



#defines charecter guess to make my life eseier
def chr_gs() :
  chr = ''.join(random.choices(string.printable, k= 1))
  return chr


#tk gui 
root = tk.Tk(screenName= None, baseName= None, className= 'Tk', useTk= 1)
root.title('Password Cracker')

#tk listbox stuff
lsbx = tk.Listbox(root)
lsbx.pack(side= 'left', fill= 'y',  expand= True)
lsbxy = tk.Listbox(root)
lsbxy.pack(side= 'left', fill= 'y', expand= True)

# tk labels
lbl = tk.Label(text = '')
lbl.pack(side= 'right', expand= True)
lbl2 = tk.Label(text = '')
lbl2.pack(side= 'right', expand= True)


#varibles 
x = 0
k = 0
pswrd = []
pswrdy = False


#gets user password
usr_pswrd = str(input("Input user password between 8 and 12 charecters long: "))
while len(usr_pswrd)  > 12 or len(usr_pswrd) < 8 :
   usr_pswrd = str(input("Input user password between 8 and 12 charecters long: "))


#actual gussing part 
while(pswrdy == False):
   #this part guesses the charecter 
   x = chr_gs()
   lsbxy.insert(tk.END, ''.join(pswrd), x)
   root.update()

   # this if verifies if the charecter is correct
   if(x != list(usr_pswrd)[k]) :
    continue

   #this bit adds a correc chaecter to a list and prints said list as a string
   print(x)
   pswrd.append(x)
   pswrdz = ''.join(pswrd)
   lsbx.insert(tk.END, pswrdz)
   lsbx.see(tk.END)

   #this changes a bool once the user input and guessed password match
   if( pswrd == list(usr_pswrd) ) :
    pswrdy = True


   #misc 
   k += 1
   lbl2.config(text= k)
   root.update()


#displays the final result
lbl.config(text= pswrdz)
lbl2.config(text= k)
root.mainloop()