



#TOOLS

#central value that a set trends toward
def mean(array):
	return sum(array) / len(array)
	
	
def std_deviation(array):
	return ( ((1/len(array))*sum([(array[i]-mean(array))**2  for i in range (len(array))]))**(1/2)	)
	
	
def frequency(array):
	history={}
	for x in array :
		history[x]=history.get(x,0)+1
	return history
	
			
	
def probability(array):
	probs={}
	for item,freq in frequency(array).items():
		probs[item]=freq/len(array)
	return probs
	
	
	
def mode_dict(dict_):
	max_val=0
	max_key=None
	for k,v in dict_.items():
		if v>max_val:
			max_key=k
			max_val=v
	return max_key
	
	

def mode_array(array):
  count={}
  for element in array:
          count.update({ element : array.count(element)})
  max_value=max(count , key=count.get)
  return max_value
  



def mean_pmf(array):
	pmf=probability(array)
	m=sum(x*p for x,p in pmf.items())
	return m
	


def variance_pmf(array):
	pmf=probability(array)
	m=mean(array)
	v=sum(p*((x-m)**2) for x,p in pmf.items())
	return v
	
	
def cond_probability(array,I,F):
	probs=[ v for k,v in probability(array).items() if I < k < F  ]
	return sum(probs)
	

	
	


