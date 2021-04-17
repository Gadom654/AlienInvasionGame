while True:
	try:
		x = int(input("First number:"))
	except ValueError:
		print("It has to be a number!")
	try:
		y = int(input("Second number:"))
	except ValueError:
		print("It has to be a number!")
	try:
		z = x + y
	except NameError:
		print("Numbers are not definied. Try again!")
	else:
		print(z)
		