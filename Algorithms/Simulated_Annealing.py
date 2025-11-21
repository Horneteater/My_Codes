

#minimize function f(x) = abs(x) 

import random
import math



def minimumize (f,T,T_min,a) :

  cur = random.uniform(-10,10)
  
 


  while T > T_min :
    cand = cur + random.uniform(-T,T)
    d = f (cand) - f (cur)
    
  
    if d <= 0 :
      cur = cand 
    else :
      p = math.exp(-d/(T))
      if random.random() < p :
        cur = cand
    T *= a
    
  return cur
 
  

T = 1000
T_min = 0.007
a = 0.9998
k=50 #spring constant


  
#spring potential energy      
def U(x):
   return ((1/2) * k * (x**2))
   
#problem: find the rest state (minimum potential energy) of a spring
print(minimumize(U,T,T_min,a))


#should be a number close to zero


