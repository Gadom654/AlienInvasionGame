answer = "idk"
while answer != "END":
	age=int(input("What's your age?\n"))
	if age<3:
		print("You'r ticket is free.")
	elif age<=12:
		print("You't ticket cost 10$.")
	elif age>12:
		print("You'r ticket cost 15$.")
	answer=input("If you want to END write END.\n")