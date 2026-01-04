

# fibonacci sequence up to N generated iteratively
#inclusive of N
#fastest for sequence
#fast doubling is best for specific nth fibonacci number

def fibonacci_sequence(N):
	a,b=0,1
	fibs=[]
	while a<= N:
		fibs.append(a)
		a,b=b,a+b
	return fibs
	
	
print(fibonacci_sequence(1000))	