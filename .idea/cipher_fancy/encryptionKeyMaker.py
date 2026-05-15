import random
import string
import json

alph = string.ascii_letters

enlib = random.sample(string.printable, len(alph))

enkey =  dict(zip(alph, enlib))

dekey = {value: key for key, value in enkey.items()}

with open("key.json", "w") as f:
    json.dump(dekey, f)

print(enkey)
print(dekey)
