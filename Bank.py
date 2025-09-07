
#simple banking app

#loan

balance=0
friend_balance=0

while True:
	
	print("""
	press:
	0.Exit program
	1.show balance
	2.deposit
	3.withdraw
	4.send money
	5.Loan
	""")
	mode=input()
	if mode == "0" :
		break
	
	if mode == "1":
		print(f"your balance is : {balance}")
		
	if mode == "2":
		deposit = float(input("amount to deposit:   "))
		balance = balance + deposit
		print("balance")
	if mode == "3" :
		withdraw=float(input("withdraw amount:  "))
		if balance < withdraw :
			print("insufficient funds")
		else:
			balance = balance - withdraw
	
	if mode == "4" :
	  send = float (input("amount to send:  "))
	  if balance > send :
	    friend_balance += send
	    balance -= send
	  else:
	    print("inadequate funds")
	    
	if mode == "5"	:
	  print("""
	  the bank offers a Loan of any amount with 6% annual interest and monthly repayments over 36 months.
	  """)
	  P=float(input("amount of money loaned:  "))
	  r=0.005 #6/12 #monthly interest
	  n=36
	  #monthly payment
	  M=P*((r*((1+r)**n))/(((1+r)**n)-1))
	  #total repayment
	  TR=M*n
	  #total interest paid
	  TIP=M*n-P
	  print(f"monthly repayment is {M} dollars")
	  print(f"total repayment is {TR} dollars")
	  print(f"total interest paid is {TIP} dollars")
	  
		   
		
print(balance)	
print(friend_balance)

	
	
	
		