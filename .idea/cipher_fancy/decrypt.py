import json


inmsg = input('input encrypted message')
with open("key.json", "r") as f:
    key = json.load(f)
msg = []
outmsg = ''

for i in inmsg : 
    if i == ' ' :
        msg.append(' ')
    else : 
        msg.append(key[i])

outmsg = ''.join(msg)

print(outmsg)

