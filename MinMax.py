

#manual implementation of minimum and maximum value

array=[7,5,1,2,-1,-2,9,0,5,2]

def minimum(array):
	min=array[0]
	for i in array :
		if i <= min :
			min=i
	return min
	
print(minimum(array))	

def maximum(array):
	max=array[0]
	for i in array:
		if i >= max:
			max=i
	return max

		
print(maximum(array))		