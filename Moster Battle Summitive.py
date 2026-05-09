import random

#initlize m1 variables

m1Hp = int(0)
m1Atk = int(0)
m1Def = int(0)
m1Spd = int(0)
m1Points = int(100)


#Functions go here
#def health() : 
 # m1Hp = int(input((m1Name, "'s health")))
 # m1Points = m1Points - m1Hp

#def atk() : 
#  m1Atk = int(input((m1Name, "'s attack")))
  #m1Points = m1Points - m1Atk
 ## return m1Atk, m1Points

#def defence() :
 #m1Def = int(input((m1Name, "'s defence")))
  #m1Points = m1Points - m1Def
 # return m1Def, m1Points

#def spd() : 
 # m1Spd = int(input((m1Name, "'s speed")))
  #m1Points = m1Points - m1Spd  
  #return m1Spd, m1Points

#def m1attack() : 
#  m1AtkValue = random.randrange(10, 100) + m1Atk
#  m1Hit = bool(m1AtkValue > m2Def)


#def m2attack() : 
 # m2AtkValue = random.randrange(10 , 100) + m2Atk
 # m2Hit = bool(m2AtkValue > m1Def)


#enemy monster stuff

m2Name = "jeff"
m2Hp   = int(25)
m2Atk  = int(25)
m2Def  = int(26)
m2Spd  = int(24)



#monster customization


m1Name = input("your monster's name: ")

print("choose you moster's skills you have 100 total points")
m1Hp = int(input((m1Name, "'s health")))
m1Points = m1Points - m1Hp
if(m1Points < 1) : print("math idiot")



m1Atk = int(input((m1Name, "'s attack")))
m1Points = m1Points - m1Atk
if(m1Points < 1) : print("math idiot")

m1Def = int(input((m1Name, "'s defence")))
m1Points = m1Points - m1Def
if(m1Points < 1) : print("math idiot")

m1Spd = int(input((m1Name, "'s speed")))
m1Points = m1Points - m1Spd
if(m1Points < 1) : print("math idiot")



#setup
dmg1 = random.randrange(30,50) - m2Def 
dmg2 = random.randrange(30,50) - m1Def 
dmg1 = int(dmg1)
dmg2 = int(dmg2)

m1Turn = bool(m1Spd > m2Spd)
m2Turn = bool(m1Spd < m2Spd)

print(m1Hp)
print(m2Hp)
m2AtkValue = random.randrange(10 , 100) + m2Atk
m2Hit = bool(m2AtkValue > m1Def)
m1AtkValue = random.randrange(10, 100) + m1Atk
m1Hit = bool(m1AtkValue > m2Def)

while((m1Hp) and (m2Hp) >= 1):
 if( m1Hit == True ) :
       m2Hp = m2Hp - dmg1 
       print(m1Name, " attacks! jeff's health is now", m2Hp)
 if( m2Hit == True ) :
       m1Hp = m1Hp - dmg2 
       print("jeff attacks! ", m1Name, "'s health is now", m1Hp)
   # if(m1Spd > m2Spd, m1Hit) : m2Hp = m2Hp - dmg1, print(m1Name, " attacks! jeff's health is now", m2Hp)