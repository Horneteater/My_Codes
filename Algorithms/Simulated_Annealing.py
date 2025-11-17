

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
def f(x) :
	return abs(x)
  
      
 
print(minimumize(f,T,T_min,a))





