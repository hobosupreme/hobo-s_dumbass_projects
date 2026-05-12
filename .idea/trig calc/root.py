import tkinter as tk

root = tk.Tk(screenName=None, baseName=None, className='Tk', useTk=1)
root.title('trig calculator_main')


def clear(event):
    if tkusrin.get() == 'input':
        tkusrin.delete(0, tk.END)
        tkusrin.config(fg='black')


tkusrin = tk.Entry(root, )
tkusrin.insert(0, 'input')
tkusrin.bind("<FocusIn>", clear)
tkusrin.pack()


tan = tk.Button(root, text='tan', )
tan.pack(side='bottom', expand=True)

cos = tk.Button(root, text='cos', )
cos.pack(side='bottom', expand=True)

sin = tk.Button(root, text='sin', )
sin.pack(side='bottom', expand=True)


root.mainloop()
