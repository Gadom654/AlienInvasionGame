users = []
if users:
	for user in users:
		if user == "admin":
			print("Welcome admin! Do you want to see raport from today?")
		else:
			print("Welcome ", user,"! Thank's for logging in again.")
else:
	print("We need to find users!")