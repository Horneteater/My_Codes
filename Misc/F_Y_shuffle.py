
#Fisher-Yates shuffling algorithm

import random

def shuffle(array):
	#random values to be used as 
	rand_values = [random.random() for i in range(len(array))] 
	#indexes to be sorted by rand values
	rand_index = [i for i in range(len(array))]
	# sort indexes by i that is the random values
	rand_index.sort(key= lambda i : rand_values[i])
	# array has i replaced by the new random index
	arr=[array[i] for i in rand_index]
	return arr
	
a=[i for i in range (10)]
print(shuffle(a))	
	