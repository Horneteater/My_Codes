
#aircraft trajectory for smooth fligh using spline with scipy

#spline returns a function that passess through those waypoints



from scipy.interpolate import make_interp_spline as spline
import matplotlib.pyplot as plt
import numpy as np

#waypoints

#at these times
t_points=np.array([i for i in range(100+1)])
# X should be these spots
x_points=np.array([i*2 for i in range(len(t_points))]) 

#make it a polynomial spline
x_spline=spline(t_points,x_points,k=5)

def x(t):
  return x_spline(t)


L=max_height=10 #km
k=4/t_points[-1]
x0 = t_points[-1]/2
def sig(i):
  sigmoid=((L)/(1+np.exp(-k*(i-x0))))
  return sigmoid

#and Z should be these spots  
z_points=np.array([sig(i) for i in t_points])

#again making it a polynomial spline
z_spline=spline(t_points,z_points,k=5)

def z(t):
  return z_spline(t)	
  



#now to visualize

tt=np.linspace(0,t_points[-1],500)
xx=[x(i) for i in tt]
zz=[z(i) for i in tt]


plt.plot(xx,zz)
plt.xlabel("X(decimeters))")
plt.ylabel("Z(KM)")
plt.gca().set_aspect(10)
plt.show()

  

