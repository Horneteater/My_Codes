


#error correction through repetition 

import random
from statistics import mode
import string


txt="hello world"

def repetition_codes(str):
	redundant = [[ch] * 3 for ch in str]
	#simulating error
	redundant[random.randint(0,len(redundant))][random.randint(0,2)]=random.choice(string.ascii_letters)
	#chainged a random redundancy
	corrected = [mode(letter) for letter in redundant]
	joined="".join(corrected)
	return joined

				
print(repetition_codes(txt))		