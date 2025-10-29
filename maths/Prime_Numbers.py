
import math

#nth prime number using C. P. Willans formula

def prime(n):
    nth_prime= 1+(sum((math.floor((n/(sum((math.floor((math.cos((math.pi) * ((math.factorial(j-1) + 1 ) / j))) ** 2 )) for j in range (1 , i+1 )))) ** (1/n))) for i in range (1 , (2 ** n)+1)))

    return nth_prime



def sequence(i):
    seq=[prime(i) for i in range (1, i+1)]
    return seq

print(sequence(5))
        
