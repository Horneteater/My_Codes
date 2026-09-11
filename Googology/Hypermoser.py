


"""

a program to calculate hyper moser and other mega numbers

sources:
    
https://youtu.be/Jw_ZPdnHGzg?is=OPv6G4OvfEtFMTLO   

https://googology.fandom.com/wiki/Steinhaus-Moser_Notation  


"""

def triangle(n):
    return n**n
    

def square(n):
    s=n
    for _ in range(n):
        s=triangle(s)
    
    return s


def circle(n):
    c=n
    for _ in range(n):
        c=square(c)
    
    return c
    
    
mega=circle(2)    
triton=circle(3)
megiston=circle(10)

#Leo Moser definition
def Pentagon(n):
    p=n
    for _ in range(n):
        p=square(p)
    
    return p
    
def Hexagon(n):
    h=n
    for _ in range(n):
        h=pentagon(h)
    return h
    
    
A_ooga=Hexagon(n)


def polygon(n,level):
             
             if level == 3 :
                 return n**n
             
             r=n
             for _ in range(n):
                 r=polygon(r,level-1)
                 
             return r
             
             
             
             
moser=polygon(2,mega)  
grand_moser=polygon(3,mega)  
great_moser=polygon(4,mega)
super_moser=polygon(2,moser)

def supertower(i):
    d=super_moser
    for _ in range(i):
        d = polygon(2,d)
    return d


#Ladies and Gentlemen I present to you the one and only

Hyper_Moser=polygon(2,supertower(moser))