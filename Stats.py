
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