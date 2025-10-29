
#encryption

#encrypt a string using caesar's cipher



def encryption(text,shift=3):
	enc=[]
	for i in text:
		i=ord(i)+shift
		enc.append(i)
	enc2=[]
	for l in enc:
		l=chr(l)
		enc2.append(l)
    
	enc3="".join(enc2)
    
	
	return enc3
	

	

def decryption(text,shift=3):
	shift=-shift
	enc=[]
	for i in text:
		i=ord(i)+shift
		enc.append(i)
	enc2=[]
	for l in enc:
		l=chr(l)
		enc2.append(l)
	enc3="".join(enc2)
	return enc3		
			
txt=str(input(" what massage is to be encrypted:  "))				
						
key=int(input("please enter a key as integer:  "))
	
encrypted_text=encryption(txt,key)
decrypted_text=decryption(encrypted_text,key)


print(txt)
print(encrypted_text)
print(decrypted_text)
