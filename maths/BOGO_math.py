
#bogo math
# a brute force approach that gives random answers untill correct one

# x+1=4
# solve for x

import random

#initial guess
x=random.randint(-100000,100000)

counter=0

while x+1 != 4 :
	x=random.randint(-100000,100000)
	counter += 1
	
print(x)	
print(counter)
	
	
