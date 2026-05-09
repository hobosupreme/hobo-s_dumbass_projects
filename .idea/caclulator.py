
#misc pre operation declarations and stuff
a = 0
b = 0
# functions for later use
def add() :
     global a 
     a += b

def sub() :
     global a 
     a -= b

def mult() :
     global a 
     a *= b

def div() :
     global a 
     a /= b

def usr_input() :
    global a, b, op
    a = int(input("Input first number: "))
    b = int(input("Input second number: "))
    op = str(input("Input Operator: "))

#execution
# usr_input()
# def calculate() :
#      a = gui.entry1.get()
#      b = gui.entry2.get()
#      if(gui.v == 1) : 
#           add()
#           print(a)

#      elif(gui.v == 2) : 
#           sub()
#           print(a)

#      elif(gui.v == 3) : 
#           mult()
#           print(a)

#      elif(gui.v == 4) : 
#           div()
#           print(a)
