
"""

a humorous sorting algorithm that generates all permutations of a sequence then checks them one by one to see if it is sorted.

Brute Force approach.Extremely inefficient. Estimated Run time of 

O (n! + n!*n)

n! for generating the permutations and loops to go over the n! generated permutations n times checking each element for order


"""


def Perm_Sort(array):
	def Permutations(arr):
		if len(arr) <= 1 :
			return [arr]
		permutations = []
		for i in range (len (arr)):
			perms = Permutations ( arr [:i] + arr [i +1 :])
			for p in perms:
				permutations.append([arr[i], *p])
		return permutations
	
	def isSorted(arr):
		if len(arr) <= 1 :
			return True
		for i in range (1,len(arr)):
			if arr[i-1] > arr[i] :
				return False
		return True 
	
		
		
	for a in Permutations(array):
	  if isSorted(a) :
			 return a
	return None
		
	

	
	  
	
print(Perm_Sort([2,3,1]))