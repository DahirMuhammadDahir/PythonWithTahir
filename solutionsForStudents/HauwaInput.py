

# defining the hot guys functions
# note that if you want the code to take in real names you have to modify it 
# to do so instead of checking for 'a' and 'b'

def hot_guys(guy_name):  # note that arugment could be anything it doesn't matter the name
	# at this point you are checking if the user entered 'a' as his name
	if guy_name == 'a':
		print("stefan is totally hot")

	# here you are checking if the user entered 'b' as his name
	elif guy_name == 'b':
		print("Timothee is hot")

	# lastly you are checking for any other input apart from a and b
	else:
		print("who are you")


guy_name = input("enter your name:\n")
hot_guys(guy)
