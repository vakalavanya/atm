balance=10000

def display_balance():
	print(f"your current balance is {balance}.")

def deposit_money():
	global balance
	amount=int(input("Enter the amount to deposit:"))
	balance+=amount
	print(f"Deposit of {amount} successful.")
	display_balance()

def withdraw_money():
	global balance
	amount=int(input("enter the amount to withdraw:"))
	if amount>balance:
		print("Insufficient balance.")
	else:
		print("Avaialable notes:100,200,500,2000")
		notes=[int(x)for x in input("Enter the notes you require(separated by space):").split()]
		total_amount=sum(notes)	
		if total_amount !=amount:
			print("Invalid notes provided.")
		else:
			balance-=amount
			print("Please collect your cash.")
			display_balance()
while True:
		print("Welcome to te ATM.")
		print("1.Display balance")
		print("2.Deposit money")
		print("4.Quit")
		choice=int(input("Enter your choice:"))

		if choice==1:
			display_balance()
		elif choice==2:
			deposit_money()
		elif choice==3:
			withdraw_money()
		elif choice==4:
			print("THANK YOU FOR USING THE ATM")
			break
		else:
			print("Invalid choice.")
			

