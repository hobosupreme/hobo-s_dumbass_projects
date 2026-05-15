import encryptionKeyMaker
import string


enkey = encryptionKeyMaker.enkey
inmsg = input('input message')
msg = []
outmsg = ''
for i in inmsg : 
    if i == ' ' : 
        msg.append(' ')
    else : 
        msg.append(enkey[i])

outmsg = ''.join(msg)
print(outmsg)  