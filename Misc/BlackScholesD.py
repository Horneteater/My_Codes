
"""
Black Scholes eq for European (discreet) options

"""

#Cumulative distribution function. i dunno it read so at docs
from scipy.stats import norm as N
from math import exp,log,sqrt



def C(S,K,r,t,V):
	"""
	parameters are:
	
	C : option price
	K : strike price
	S : current stock price
	r : risk free interest rate
	t : time to maturity
	
	"""
	
	d1 =( log(S/K) + (r + ((V**2)/2) ) * t  ) / (V * sqrt(t))
	
	d2= d1 - V * sqrt(t)
	
	c= S*N.cdf(d1) - K*exp(-r*t) * N.cdf(d2)
	
	return c
	
	