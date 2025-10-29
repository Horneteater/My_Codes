
# XOR cipher

#encryption by breaking down the input and key to its 01010 bits and doing and doing XOR operation on every bit of input against every bit of key to get a new set of bits


def encryption (text,key=3):
	
	#prerequisites
	assert isinstance(text,str), "text must be string"
	
	assert isinstance(key,int),"key must be integer"
	
	
	
	
	key %=256 #for byte (256) match our key must not be higher than 256 or 0
	assert key !=0 and key !=256 #wont change anything if so
	
	
	#encryption logic
	enc=[]
	for ch in text:
		ch=chr(ord(ch)^key)
		enc.append(ch)
		
	enc2="".join(enc)
	
	return enc2
	
def decryption(text,key=3):
	
	#preconditions
	assert isinstance(text,str),"text must be string"
	
	assert isinstance(key,int),"key must be integer"
	
	key %=256 #for byte (256) match our key must not be higher than 256 or 0
	assert key !=0 and key !=256 #wont change anything if so
	
	#decryption logic
	# xor logic again back to square one
	
	dec=""
	for ch in text:
		dec += chr(ord(ch) ^ key)
		
	return dec
	
txt=str(input("what do you want to encrypt?  "))
en=encryption(txt)
dc=decryption(en)


print(txt)
print(en)
print(dc)
		
		
	
	