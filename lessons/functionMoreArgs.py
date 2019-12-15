
username = "Maimuna"
password = "password123"

username1 = "Tahir"
password1 = "password"

def login(usrname, passwd):
	func_username = usrname
	func_password = passwd
	if usrname == "Maimuna" and passwd == "password123":
		print("=====[ Access Granted ]=====")
		print(func_username)
		print(func_password)
		print(username1)
		print(password1)
	else:
		print("=====[ Access Denied ]======")


login(username, password)
