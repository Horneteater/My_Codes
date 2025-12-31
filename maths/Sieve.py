

#sieve of eratosthenes


def sieve(n):
	prime=[False]*2 +[True]*(n-1)
	p=2 #first prime
	
	while p**2 <= n:
		if prime[p]:
			for i in range(p*p,n+1,p):
				prime[i]=False
		p+=1
	
	remaining=[]
	for p in range(n+1):
		if prime[p]:
			remaining.append(p)
		
	

	return remaining
	
	
	
print(sieve(1))