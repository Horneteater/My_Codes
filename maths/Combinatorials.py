
#combinatorial algorithms


#cartesian product of unknown number of elements using iteration
def cartesian_product(array_of_arrays):
	result=[()]
	for array in array_of_arrays:
		new_result=[]
		for partial in result:
			for element in array:
				new_result.append(partial+(element,))
		result=new_result
	return result
	

A=[
[i for i in range (100,120)],
[i for i in range (10)]
]
print(cartesian_product(A))


###permutations###

# n elements may form n! permutations


#all possible permutations of an array

from itertools import product

	
def permutations(arr):
	res=[]
	for i in product(arr,repeat=len(arr)):
		if len(set(i))==len(arr):
			res.append(i)
	return res
	
print(permutations([1,2,3]))	


#combinations

def combinations(arr,r):
	res=[]
	for i in product(arr,repeat=r):
		if len (set(i)) == r and sorted(i) not in [sorted(j) for j in res]:
			res.append(i)
	return res
	
print(combinations(['A','B','C','D','E'],3))	
