


def time_dilation(T2,v):
	
	'''
	calculates time difference based on movement speed using Time dilation formula
	
	please input time in days for the stationary observer and speed of the traveler as meter per second
	'''
	
	#speed of light
	c=299_792_458 #meters per second
	
	#lorentz factor
	gamma = 1 / (1- ((v**2)/(c**2))) ** 0.5
	
	#subjective time as in time on the moving object is T1
	#time on stationary observer is T2
	T1 = T2/gamma
	
	return f" time has passed {T2} days on earth while {T1} days has passed on the ship "
	
#apollo 11	
print(time_dilation(8,11265.408))	