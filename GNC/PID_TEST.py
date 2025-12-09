

#simulated pid controller


#proportion for error correction now , integral for past errors, derivate for future errors

#proportional error correction is P*e where p is a tunable parameter and e is error. correction is applied change proportional to the error



#integral #correction for sum of past errors

#derivate #correction for future errors

#why sum them not other things like average?
#because it's combination of corrective error

#discrete pid measured at every second (simulated with random)

#it's not returning correct answers because the model itself, randomized error can't be accurately simulated with PID, Our Error and U are largely independent.

import random
import time
import math



#mimimize abs( u(kp,ki,kd) - e ) with Annealing
#so I minimized the difference between correction and error 

	
#my custom Simulated Annealing
def minimumize (f,T=100,T_min=0.007,a=0.98) :

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




	
			
#begin PID

#parameterization

		
def f_kp(Kp):
				
  E=[0]
  U=[]
  for i in range(1000):
	
    Ts=1/3#sampling frequency( samples per secomd)
    SP=50 #setpoint #where we want to be
     
    PV=random.uniform(SP-10 , SP+10) #process variable #where we are #read from sensor #simulated with random here
    e=SP-PV
    E.append(e)
    #anti windup
    if len(E) > 7:
      E.pop(0)

    Ki = 1 #tuneable parameter for integration
    Kd = 1 #tuneable parameter for derivation
    #controller output at K th time
    u=(Kp * E[-1]) + (Ki * Ts * (sum(E) ))+ (Kd *( (E[-1]-E[-2])/Ts))
    U.append(u)
    #by applying u to the system we get the  desired result
  result=sum(U)-sum(E)
  return result  
  
  
Kp=minimumize(f_kp)

def f_ki(Ki):
				
  E=[0]
  U=[]
  for i in range(1000):
	
    Ts=1/3#sampling frequency( samples per secomd)
    SP=50 #setpoint #where we want to be
     
    PV=random.uniform(SP-10 , SP+10) #process variable #where we are #read from sensor #simulated with random here
    e=SP-PV
    E.append(e)
    #anti windup
    if len(E) > 7:
      E.pop(0)
    
    Kd = 1 #tuneable parameter for derivation
    #controller output at K th time
    u=(Kp * E[-1]) + (Ki * Ts * (sum(E) ))+ (Kd *( (E[-1]-E[-2])/Ts))
    U.append(u)
    #by applying u to the system we get the  desired result
  result=sum(U)-sum(E)
  return result 
  
Ki=minimumize(f_ki)    



def f_kd(Kd):
				
  E=[0]
  U=[]
  for i in range(1000):
	
    Ts=1/3#sampling frequency( samples per secomd)
    SP=50 #setpoint #where we want to be
     
    PV=random.uniform(SP-10 , SP+10) #process variable #where we are #read from sensor #simulated with random here
    e=SP-PV
    E.append(e)
    #anti windup
    if len(E) > 7:
      E.pop(0)

    #controller output at K th time
    u=(Kp * E[-1]) + (Ki * Ts * (sum(E) ))+ (Kd *( (E[-1]-E[-2])/Ts))
    U.append(u)
    #by applying u to the system we get the  desired result
  result=sum(U)-sum(E)
  return result 
  
Kd=minimumize(f_kd)    

E=[0]

while True:
	
  Ts=1/3#sampling frequency( samples per secomd)  
	
  time.sleep(3)
  
  SP=50 #setpoint #where we want to be


  PV=random.uniform(SP-10 , SP+10) #process variable #where we are #read from sensor #simulated with random here

  
  
  e=SP-PV
  E.append(e)
  #anti windup
  if len(E) > 7:
    E.pop(0)


  #controller output at K th time
  u=(Kp * E[-1]) + (Ki * Ts * (sum(E) ))+ (Kd *( (E[-1]-E[-2])/Ts))
  
  
 
  
  print(u)

  #by applying u to the system we get the  desired result




