import string
alph = string.ascii_letters
x = dict()
rotX = 1
y = []
out = ''
for i in alph :
    y = ord(i) + rotX
    x.update({i : chr(y)})


msg = input('please input your message')

for i in msg :
    if  i == string.whitespace :
        continue
    else :
        y.append(x[i])