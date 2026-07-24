
"""

aircraft flight modeled with bernoulli equation

WARNING: simplified model, not full explanation

the pressure difference explaination of flight

FYI any unit is applicable so long as it's consistent across both sides of the equation

glossary of terms:

P is pressure in pascal (Pa) units
r is density in (Kg/m3) units
g is gravitational acceleration (9.81) in (m/s2)
h is height in meters
v is velocity in (m/s)


bernoulli equation:

two sides must have same dimensions

because conservation of energy:
energy density at one side == energy density at the other side

p1 + r*g*h1 + (1/2) * r * (v1 ** 2)  ==

p2 + r*g*h2 + (1/2) * r * (v2 ** 2)

I'll model as three regions front, above and below the airfoil, find the pressure diffrence between above and below the airfoil with two bernoulli eqations between front and above & another for front and below

data will be gathered empirically (googled)

rgh has negligible diffrence thus is discarded

I'm using a Boeing 737 as my model
assumptions:
	air flow is 20% faster above wing
	wing area= 102 m2
	velocity=67 m/s assuming takeoff speed

"""

from sympy import symbols , Eq , solve

#solves for pressure
def bernoulli(p1,r,v1,v2):
	
	p2=symbols('p2')
	
	equation=Eq(p1 + (1/2) * r * (v1 ** 2)  , p2 + (1/2) * r * (v2 ** 2) )
	
	pressure_P2 = solve(equation,p2)
	return pressure_P2


#values

	
r= 1.225 #air density


p_front= 101325 #pa
p_above= 101325 #pa
p_below= 101325 #pa

v_front=67 #m/s
v_above=67 + (20/100) * 67
v_below= 67 + (10/100) * 67

airfoil_area=102 #Boeing 737


p_above = bernoulli(p_front,r,v_front,v_above)[0]
	
	
p_below = bernoulli(p_front,r,v_front,v_below)[0]
	
	
pressure_diff =   p_below - p_above
	
force = pressure_diff * airfoil_area
	

	
	
print (f"pressure above the wing: {int(p_above)} \n pressure below the wing:  {int(p_below)} \n pressure difference:  {int(pressure_diff)} \n force generated upwards : {int(force)}")
	
	
	
	