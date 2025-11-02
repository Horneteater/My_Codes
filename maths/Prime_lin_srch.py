

#prime numbers by binary search


#sequence of prime numbers up to specified integer
def prime_sequence(n : int)  -> list :
	
	def is_prime(m):
		for j in range (2,m):
			if m%j == 0:
				return False
		else:
			return True
		
	sequence=[]
	for i in range(2,n):
		if is_prime(i):
			sequence.append(i)
	
	return sequence
	
	
print(prime_sequence(30))		