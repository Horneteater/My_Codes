
from sympy import symbols,Eq,solve

# formula for calculating the properties of ideal gasses
#  PV=nRT 
print("calculating ideal gas property using it's formula PV=nRT")
print("All inputs must be SI units, outputs are SI standards")


wh=str(input("P for Pressure,V for volume,n for number of moles, T for temperature.  ")).upper()




P,V,n,R,T=symbols('P V n R T')

if wh=="P":
	
	Vi=float(input("volume of the gas(m**3):  "))
	
	ni=float(input("number of moles(n):   "))
	
	Ti=float(input("Temperature(k):    "))
	
	Ri=8.314
	
	eqMain=Eq(P*V,n*R*T)
	
	eq_subss=eqMain.subs({V:Vi,n:ni,T:Ti,R:Ri})
	
	#solved in 3 steps as each step is s
	s1=solve(eq_subss,P)
	
	s2=s1[0]
	
	s3=f"pressure is {s2} pascals"

	final=s3
	
elif wh=="V":
	
	Pi=float(input("pressure(Pa):     "))
	
	ni=float(input("number of moles(n):   "))
	
	Ti=float(input("Temperature(K):    "))
	
	Ri=8.314
	
	eqMain=Eq(P*V,n*R*T)
	
	eq_subss=eqMain.subs({P:Pi,n:ni,T:Ti,R:Ri})
	
	#solved in 3 steps as each step is s
	s1=solve(eq_subss,V)
	
	s2=s1[0]
	
	s3=f"volume is {s2} meters qubed"


	final=s3
	
elif wh=="n":
	Vi=float(input("volume of the gas(m**3):  "))
	
	Pi=float(input("pressure(Pa):     "))
	
	Ti=float(input("Temperature(K):    "))
	
	Ri=8.314
	
	eqMain=Eq(P*V,n*R*T)
	
	eq_subss=eqMain.subs({V:Vi,P:Pi,T:Ti,R:Ri})
	
	#solved in 3 steps as each step is s
	s1=solve(eq_subss,n)
	
	s2=s1[0]
	
	s3=f"number of moles in the gas is {s2} "
	
	
	

	final=s3
	

elif wh=="T":
	Vi=float(input("volume of the gas(m**3):  "))
	
	ni=float(input("number of moles(n):   "))
	
	Pi=float(input("pressure(Pa):     "))
	
	Ri=8.314
	
	eqMain=Eq(P*V,n*R*T)
	
	eq_subss=eqMain.subs({V:Vi,n:ni,P:Pi,R:Ri})
	
	#solved in 3 steps as each step is s
	s1=solve(eq_subss,T)
	
	s2=s1[0]
	
	s3=f"temperature is {s2} kelvin"
	

	final=s3
	
else:
	final="invalid value"
	
print(final)	


