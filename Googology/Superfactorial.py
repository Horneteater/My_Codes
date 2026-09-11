


def superfactorial(n):
	
	def product(list):
		p=1
		for e in list:
			p *= e
		
		return p
	
	def factorial(i):
		if i<2 :
		    return 1
		return i * factorial(i-1)
		


	return product([factorial(i) for i in range(1,n+1)])
		
			
	    
		
		
print(superfactorial(5))			