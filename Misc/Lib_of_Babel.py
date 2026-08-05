


"""


an infinite wisdom generator based on normal number specifically  π

it will take a while to run, probably much more than 10 minutes

You also need some mechanism to filter out the infinite wisdom, try maybe reading through it?

assumptions:  π is normal

https://en.wikipedia.org/wiki/Normal_number



"""

import random
from decimal import Decimal,getcontext
import time


# converting numbers into letters
def convert (num) :
	
	num = str(num)
	
	key= {
	
	"1" : ["a","b"],
	"2" : ["c","d","e"],
	"3" : ["f","g"],
	"4" : ["h","i","z"],
	"5" : ["j","k"," "],
	"6" : ["l","m","."],
	"7" : ["n","o"],
	"8" : ["p","q","r"," "],
	"9" : ["s","t","u","v"],
	"0" : ["w","x","y"],
	"." : [""]
	
	
	}
	
	return random.choice(key[num])
	
	
# I copied this one from my previous project I'm really sorry
#The Bailey–Borwein–Plouffe formula (BBP formula) for π.



#prc is precision, the number of digits of pi you want
def pi(prc):
        getcontext().prec=prc
        pi=Decimal(0)
        for k in range(prc):
                 pi = pi + (Decimal(1) / Decimal(16)**k) * (
            Decimal(4) / (8*k + 1)
            - Decimal(2) / (8*k + 4)
            - Decimal(1) / (8*k + 5)
            - Decimal(1) / (8*k + 6)
        )

        return +pi 
        
      


n=3
while True:
	print("".join([convert(n) for n in str(pi(n))]))
	n += 1
	time.sleep(0.3)