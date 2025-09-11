

#model sunspot activity as markov chains

import pandas as pd
import numpy as np

np.set_printoptions(suppress=True)

columns=[ "year" , "month" , "day" , "year fraction" , "sunspotnumber" , "sunspot number deviation","number_of_observations" ,"provisional_indicator" ]

url="https://www.sidc.be/SILSO/INFO/sndtotcsv.php"

#official SIDC numbers
df=pd.read_csv(
url,
sep=";" ,
header=None ,
 names = columns
 )



data=df['sunspotnumber']

##################################

#low to low transition 

low_count=0
for i in range(len(data)-1):
  if 0 <= data[i] <=20 and data[i+1] != -1 :
    low_count += 1


#low to low transition count
LTLC = 0 

for i in range (len(data)-1):

  if 0 <= data[i] <= 20 and  0 <= data[i+1] <= 20:
	  LTLC += 1

#low to low transition probability
LTLP= LTLC / low_count 

#low to mid transition count
LTMC= 0

for i in range(len(data)-1):

  if 0 <= data[i] <= 20 and  20 < data[i+1] <= 67:
	  LTMC += 1


#low to mid transition probability
LTMP = LTMC / low_count


#low to hi transition count
LTHC = 0

for i in range(len(data)-1):

  if  0<= data[i] <= 20  and  data[i+1] > 67 :
    LTHC += 1


#Low to high transition probability
LTHP = LTHC / low_count



 
##################################



mid_count=0
for i in range(len(data)-1):
  if 20 < data[i] <= 67 and data[i+1] != -1 :
    mid_count += 1


#mid to low transition count
MTLC = 0 

for i in range (len(data)-1):

  if 20 < data[i] <= 67 and  0 <= data[i+1] <= 20:
	  MTLC += 1

#mid to low transition probability
MTLP= MTLC / mid_count 

#mid to mid transition count
MTMC= 0

for i in range(len(data)-1):

  if 20 < data[i] <= 67 and  20 < data[i+1] <= 67:
	  MTMC += 1


#mid to mid transition probability
MTMP = MTMC / mid_count


#mid to hi transition count
MTHC = 0

for i in range(len(data)-1):

  if  20 < data[i] <= 67  and  data[i+1] > 67 :
    MTHC += 1


#Low to high transition probability
MTHP = MTHC / mid_count




##################################



hi_count=0
for i in range(len(data)-1):
  if data[i] > 67 and data[i+1] != -1 :
    hi_count += 1


#hi to low transition count
HTLC = 0 

for i in range (len(data)-1):

  if  data[i] > 67 and  0 <= data[i+1] <= 20:
	  HTLC += 1

#hi to low transition probability
HTLP = HTLC / hi_count 

#hi to mid transition count
HTMC= 0

for i in range(len(data)-1):

  if data[i] > 67 and  20 < data[i+1] <= 67:
	  HTMC += 1


#hi to mid transition probability
HTMP = HTMC / hi_count


#hi to hi transition count
HTHC = 0

for i in range(len(data)-1):

  if  data[i] > 67  and  data[i+1] > 67 :
    HTHC += 1


#Low to high transition probability
HTHP = HTHC / hi_count



##################################
#transitions are daily updates so n represents days

#transition_matrix
#the probability of transition from states to states
TM = np.array( [
[LTLP,LTMP,LTHP],
[MTLP,MTMP,MTHP],
[HTLP,HTMP,HTHP]
])



#initial state
#the state(s) we begin at
# the sunspot number of today

current_state=data.iloc[-1]

assert current_state != -1 , "invalid value"

if 0 <= current_state <= 20 :
  S0=np.array([
[1],
[0],
[0]
])

if 20 < current_state <= 67 :
  S0=np.array([
[0],
[1],
[0]
])

if 67 < current_state  :
  S0=np.array([
[0],
[0],
[1]
])

#number of iterations days in this case
#the days from now we are predicting
#arbitrary value
n=7



             

#Sn = (P**n) * S0

Sn= np.linalg.matrix_power(TM, n) @ S0



Sn = Sn.flatten() #for numpy weirdness

#normalization
#divide each element by the sum of all elements
#so each element is represented as the fraction of the whole
Sn = Sn / np.sum(Sn) 


FS1=Sn[0]*100
FS2=Sn[1]*100
FS3=Sn[2]*100

Final_string=f" on the given day probability of Low sunspot activity is {FS1}% ,medium sunspot activity is {FS2}% and the probability of heavy sunspot activity is {FS3}% "

assert 95 < FS1+FS2+FS3 < 105 , "only 10 percent error range acceptable"
print(Final_string)
