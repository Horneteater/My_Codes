

#random gibberish

import random
import string
b=string.printable
r=random.randrange(0,len(b))
c=random.choices(b,k=r)
print("".join(c))
