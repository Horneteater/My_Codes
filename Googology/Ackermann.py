
def hypop(a,n,b):
    #knuth's up arrow notation
    assert type(a) is int and type(n) is int and type(b) is int and a >=0 and n >= 1 and b >= 0 , "incorrect values"
    if n==1 :
        return a**b
    
    if n>1 and b==0 :
        return 1
    
    
    return hypop(a,n-1,hypop(a,n,b-1))
    
    

def Ackermann_number(n):
    
    return hypop(n,n,n)
    
