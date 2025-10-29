
#Linear Congruential Generator (LCG) Algotithm

# I got the correct parameters and formula from java.util.Random Number Generator

import time

#define seed as float to get a float
def random_int(seed):


    a=25214903917#multiplier 

    c=11 #increment 

    m=2**48 #modulus

    return (a*seed+c)%m
    
    

def random_float(seed):
	
	
    a=25214903917#multiplier 

    c=11 #increment 

    m=2**48 #modulus

    randint=(a*seed+c)%m
    
    return randint/m
    

def random_sequence(length_of_sequence,seed):
            
            sequence=[]
            cur_seed=seed
            for e in range(length_of_sequence):
              next_element=random_int(cur_seed)
              sequence.append(next_element)
              cur_seed=next_element
              
            return sequence	
            
s=int(time.time()) #seed from time
l=5 #length of sequence
s1=random_int(s)
s2=random_float(s)
s3=random_sequence(l,s)[-1]

print(s1)
print(s2)
print(s3)