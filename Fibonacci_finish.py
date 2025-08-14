#fibonaci sequence

def fibonacci(n):
  if n==0:
  	return 0
  elif n==1:
      return 1
  else:
      return fibonacci(n-1) + fibonacci(n-2)
      
      
print(fibonacci(6))      

def fibonacciNumbers(n):
    ans = []
    for i in range(n):
      ans.append(fibonacci(i))
    return ans
      
      
result=fibonacciNumbers(17)

print(result)
    
  	
 
  	
  	
  	

 
 
 
	
