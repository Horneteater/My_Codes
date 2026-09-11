



def Graham():
	"""
	I don't think you have enough memory to run this program, I know I didn't. lemme know if you can run it.
	"""
	
	def hypop(a,n,b):
		"""
		knuth's up arrow notation
		
		"""
		assert type(a) is int and type(n) is int and type(b) is int and a >=0 and n >= 1 and b >= 0 , "incorrect values"
		
		
		if n==1 :
			return a**b
		
		if n>1 and b==0 :
			return 1
		
		return hypop(a,n-1,hypop(a,n,b-1))
	

	
	def g(N):
		
		assert type(N) is int and N>0 ,"N must be a  natural number"
		
		
		if N==1 :
			return hypop(3,4,3)
			
		if N >= 2 :
			return hypop(3,g(N-1),3)
		
		
		
		
		
		
	return g(64)
	
print(Graham())	