


#maybe add a gui and a feature to draw arbitrary shapes before displaying their area

#1.Area Defined by Functions in Cartesian Coordinates (y = f(x))
#calculating the area under curve y==x**2

from sympy import *
from math import pi
x=symbols('x')
Total_Area=integrate(x**2,(x,0,1))

print(f'area under a curve in Cartesian Coordinates : {Total_Area}')	


#2.Area in Polar Coordinates (r = f(θ))

#How to calculate Area in Polar Coordinates (r = f(θ))

#formula for cardioid
#A=1/2integral[(r(θ))**2][from 0 to 2pi]

from scipy.integrate import quad
import math

#radius
a=2

from_=0

to_=2**math.pi

#defining the function
def f(t):
	return a+a*math.cos(t)

inte1=(quad(f,from_,to_))
integ=inte1[0]
Area=integ/2

print(f'area in polar coordinates: {Area}')






#4.Area using Double Integrals (general approach)

#claculate area of a circle using double integral general method

#t is θ
#r is radius

# Area= integral,0 to r(integral,0 to 2pi(dA))

# circle_dA=r*d(r)*d(t)

from scipy import integrate
import math

r=1

f=lambda r,t:r


circle_area,circle_error=integrate.dblquad(f,0,2*math.pi,0,r)

print(f'area of circle is about: {circle_area}')


#5.monte carlo sampling(Enclose the shape in a known rectangle, randomly sample points, and count the fraction inside.

#Area = known area * number of samples inside/ total number of samples.

#formula for a heart shape
#((y-0.75*abs(x))**2)+((0.75*x)**2)<=1

import random


N = 10000  # number of random samples
Nin= 0 #number of samples inside

for dot in range(N):
    x = random.uniform(-2, 2)#coordinates of x and y
    y = random.uniform(-2, 2)# imagine them like a box -2 to 2 in each side that's the known shape
     #shape of a heart
    if ((y-0.75*abs(x))**2)+((0.75*x)**2)<=1:
    # inside the heart shape
        Nin += 1

estimated_area = 16 * (Nin/ N)  # 16 = area of bounding box [-2,2] x [-2,2]

print(f"Estimated area using monte carlo method: {estimated_area}")




