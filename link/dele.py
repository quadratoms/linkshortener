import string
from random import choice




def idk(i):
    l=[]
    for each in range(i):
        l.append(choice(string.ascii_letters+string.digits))
    n=''.join(l)
    return n

