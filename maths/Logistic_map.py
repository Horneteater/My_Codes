
"""

X #current population #number of elements there are now #as a percentage of max population

X=(current elements) / (max elements)

max population is found by empirical observation such as recording the peak population, or environmental constraints such as enough resources for x number of population



r #growth rate # the rate of change  # if it is 2 the population doubles #if r is below 1 population is reducing

0 <= r <= 4
0 <= r < 1 #population dying
1 <= r <=3 #population converging on a point
4 => r => 3.57  #population chaotic




r= births - deaths
or 
r= Nn / (N * (1- (N/K)) )#where Nn is population next cycle, K is maximum population and N is population this cycle



Xn #population next cycle #as a percentage of max population

#main formula

Xn = r * X * (1-X)



# chaos at 4 => r => 3.57


"""

from decimal import Decimal,getcontext
import time


getcontext().prec=100


#time based seeding
seed=time.time() % 1.0  #float: 0 < seed< 1

r=Decimal('3.994')
X=Decimal(str(seed))

seq=[]
for _ in range (1000):
	X=r*X*(1-X)
	seq.append(X)

print([float(y) for y in seq])



#music with chaos?

