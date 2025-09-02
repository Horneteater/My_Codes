
#statistics


#mean / average

#a number representing the center value that a set tends toward

	
def mean(array):
	
  def sum(array):
	  all=0
	  for i in array:
		  all = all+i
	
	  return all

  mean_f= (sum(array))/len(array)
  return mean_f
  
 
print(mean([1,2]))


#median

#the Middle value of a set



def median(array):
	sorted_array=sorted(array)
	length=len(array)
	mid_val=length//2
	if length % 2 == 0:
		median_f=((sorted_array[mid_val-1])+(sorted_array[mid_val]))/2
	
	if length % 2 != 0:
		median_f=sorted_array[mid_val]
	return median_f
	
print(median([1,2,3]))	




#mode

#the value that is repeated the most in an array

def mode(array):
  array=[1,1,2,2,2,3]

  count={}

  for element in array:
	  count.update({ element : array.count(element)})
	
  max_value=max(count , key=count.get)
  return max_value


	
print(mode([1,2,2,3,4]))	



#percentile

#  The x-th percentile is the value such that x percent of the values in the array are less than or equal to that value.

# E.g.  90 percentile =  10 means that 90 percent of individuals have scores of equal or less than 10




def percentile (array,num):
	"""
	num is the number that which we count the numbers below it to determine percentile.
	array is the one we are searching through
	returns the percentile we want
	
	"""
	
	array_sorted=sorted(array)
	N=len(array) 
	n=0
	for i in array_sorted:
		if i <= num:
		  n = n+1
	perc=((n/N)*100)
	return perc
	
#E.g. what percentile of students have scores less than 75 ?

scores=[12,8,0,1,99,100,71,89,91,99,65,70,54,43]

target=75

print(percentile(scores,target))							
	

def number_percentile(array,P):
  """
  array is array
  P is percentile
  returns the number that specified percentile
  is lower than
  """
  sorted_array=sorted(array)
  N=len(array)
  pos=(P/100)*N
  index=sorted_array[int(pos)]
  return index														
														
#E.g. what is the number that 75 percent of students got lower than

target=75


print(number_percentile(scores,75))

#probababilty
#percentege chance of an event occuring


def probability(array,target):
	occurance=0
	for i in array:
		if i==target:
			occurance = occurance + 1
	all_outcomes=len(array)
	prob=((occurance/all_outcomes)*100)
	return prob
	
# what percent chance of an index of the array to equal 3


prob_array=[1.2, 2 , 3, 3 ,4, 10.22]

print(probability(prob_array,3))




#ordinary least squares
# determines the parameters of a linear regression
#used for prediction of data




def OLS(x_axis , y_axis , X): 
    assert len(x_axis)==len(y_axis) , "x and y mismatch"
    x_bar = sum(x_axis) / len (x_axis)
    y_bar = sum(y_axis) / len(y_axis)
    r1=0 #calculating correlation Coefficient
    r2=0
    r3=0
    for i in range(len(x_axis)):
        r1 +=(x_axis[i] - x_bar) * (y_axis[i] - y_bar)
        r2 +=((x_axis[i] - x_bar)**2) 
        r3 +=(((y_axis[i] - y_bar)) **2 )
       
    r = r1 / ((r2**0.5) * (r3**0.5))
    if -0.5 < r < 0.5 :
        rx= f"correlation Coefficient is {r} . inadequate correlation"
        return rx    
    m1=0 #calculating slope of our line
    m2=0
    for i in range (len(x_axis)):
        m1 += (x_axis[i] - x_bar) * (y_axis[i] - y_bar)
        m2 += (x_axis[i] - x_bar) ** 2
    if m2 == 0:
        return y_bar
    m = m1 / m2
    a = y_bar - (m * x_bar) # the intercept point
    Y= m * X + a
    
    def resi(t): #residuals

        residual=y_axis[t]-( m * x_axis[t] + a)
        return residual
    #durbin watson test   
    d1=0 
    for i in range (1,len(x_axis)):
        d1 += ((resi(i) - resi(i-1)) ** 2)
    d2=0
    for i in range (len(x_axis)):
        d2 += resi(i) ** 2
    if d2==0:
    	d=2
    else:
        d = d1 / d2
        
    if 1.5 < d < 2.5  : #the acceptable range of D
        pass #only for the else statement
      
    else:
        dd = f"d={d}.too much correlation for OLS"
        return dd
        
    
    return Y # here our code ends


#our sample synthetic data  
x=[1,2,3,4,5,6]  
y=[]
for i in x:
	yy=5*i+5
	y.append(yy)
ff=OLS(x,y,5)
print(ff)
		