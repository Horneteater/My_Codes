
#binary converter

#converting base 10 (decimal) to base 2 (binary)





def int_binary(num):
  number=int(num)
  binary=[]

  while number  >  0 :
    bit=number%2
    binary.append(bit)
    number //= 2

  binary.reverse()

  b=0
  for bit_ in binary:
    b = b * 10 + bit_
	
  return b



def frac_binary(num):
	integ=int(num)
	frac=num-int(num)
	a,b=frac.as_integer_ratio()
	c=int_binary(a)
	d=int_binary(b)
	e=c/d
	return e
	
	
def binary(num):
	p1=int_binary(int(num))
	p2=frac_binary(num-int(num))
	f=p1+p2
	return f

print(binary(8.1))
print(binary(8))

def decimal(num):
	
	#getting the digits
	digits=[]
	while num > 0 :
		digit=num % 10
		digits.append(digit)
		num //= 10
		
	deci=[]
	for index,value in enumerate(digits):
		dec = value * (2**index)
		deci.append(dec)
	
	
	return sum(deci)

print(decimal(1000))
