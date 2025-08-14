
#pi calculator

#The Bailey–Borwein–Plouffe formula (BBP formula) for π.

from decimal import Decimal,getcontext


#prc is precision, the number of digits of pi you want
def pi(prc):
	getcontext().prec=prc
	pi=Decimal(0)
	for k in range(prc):
		 pi = pi + (Decimal(1) / Decimal(16)**k) * (
            Decimal(4) / (8*k + 1)
            - Decimal(2) / (8*k + 4)
            - Decimal(1) / (8*k + 5)
            - Decimal(1) / (8*k + 6)
        )

	return +pi #plus is for applying Decimal Precision
	

print(pi(3))

