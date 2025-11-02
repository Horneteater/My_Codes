


from sympy import symbols,Eq,solve,diff,Function


#Euler-Lagrange equation



m,g,t=symbols('m g t') #mass gravity and time

#defining q as x and y
x=Function('x')(t)
y=Function('y')(t)

#velocity as xdot and ydot
xdot=diff(x,t)
ydot=diff(y,t)

L = ((1/2)*m*(xdot**2+ydot**2)) - (m*g*y)

#equation in x axis
eq_x = Eq(diff(diff(L,xdot),t),diff(L,x))

#equation in y axis
eq_y = Eq(diff(diff(L,ydot),t),diff(L,y))

#motion vector
r=f"{eq_x} i + {eq_y} j "


print(r)










