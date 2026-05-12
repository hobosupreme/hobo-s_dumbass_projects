import tkinter as tk

root = tk.Tk(screenName=None, baseName=None, className='Tk', useTk=1)
root.title('trig calculator_main')


def clear(event):
    if tkusrin.get() == 'input pasword':
        tkusrin.delete(0, tk.END)
        tkusrin.config(fg='black')


tkusrin = tk.Entry(root, )

tkusrin.insert(0, 'input pasword')
tkusrin.bind("<FocusIn>", clear)
tkusrin.pack()


root.mainloop()
