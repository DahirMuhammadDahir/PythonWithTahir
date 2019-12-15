
bank = [

{"account_name":"Dahir Muhammad", "account_number":"001", "account_balance":30000}, 
{"account_name":"Fauziya Musa", "account_number":"002", "account_balance":70000},
{"account_name":"Aisha Ahmad", "account_number":"003", "account_balance":35000}, 
{"account_name":"Maimuna Ahmad", "account_number":"004", "account_balance":200000}

]

def main():
	while True:
		action = input("Welcome, what would like to do:\n[1] - Deposit Money \n[2] - Withdraw Money \n[3] - Transfer Money \n[4] - Check Balance \n[5] - Exit Bank\n\n")
		if action == "1":
			deposit_funds()
		elif action == "2":
			withdraw_funds()
		elif action == "3":
			transfer_funds()
		elif action == "4":
			check_balance()
		elif action == "5":
			exit()
		else:
			print("\nPlease check your inputs\n")

def deposit_funds():
	target_account_number = input("Enter target account number:\n")
	target_amount = input("Enter amount you want to deposit:\n")
	target_amount = int(target_amount)

	try_to_deposit = credit_account(target_account_number, target_amount)

	if try_to_deposit == True:
		print("\n======[ Bank Deposit was Successful]======\n")
	else:
		print("\n======[ Bank Deposit Failed]======\n")

def withdraw_funds():
	target_account_number = input("Enter target account number:\n")
	target_amount = int(input("Enter amount you want to withdraw:\n"))

	try_to_withdraw = debit_account(target_account_number, target_amount)

	if try_to_withdraw == True:
		print("\n======[ withdrawal Successful, please take your cash ]======\n")
	else:
		print("\n======[ Withdrawal Failed]======\n")


def transfer_funds():
	user_account_number = input("Enter your account number:\n")
	amount_to_transfer = int(input("Enter amount you want transfer:\n"))
	recipient_account_number = input("Enter the Receiver's account number:\n")

	try_to_debit = debit_account(user_account_number, amount_to_transfer)

	if try_to_debit == True:
		try_to_transfer = credit_account(recipient_account_number, amount_to_transfer)
		if try_to_transfer == True:
			print("\n======[ Transfer was Successful]======\n")
		else:
			print("\n======[ Transfer Failed]======\n")

	else:
		print("\n======[ Sorry we couldn't process your transfer]======\n")



def check_balance():
	target_account_number = input("Enter target account number:\n")

	for account in bank:
		if account["account_number"] == target_account_number:
			current_account_balance = account["account_balance"]
			print(f"\n======[ Your Account Balance is {current_account_balance}]======\n")
			return
	print("\nAccount Number Not found\n")


def credit_account(target_account_number, amount):
	for account in bank:
		if account["account_number"] == target_account_number:
			account["account_balance"] += amount
			return True
	return False


def debit_account(target_account_number, amount):
	for account in bank:
		if account["account_number"] == target_account_number:
			account["account_balance"] -= amount
			return True
	return False

main()