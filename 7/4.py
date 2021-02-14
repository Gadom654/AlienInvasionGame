action = True
while action:
	topping = input("Do you want to add some topping?\nIf not write END.\n")
	if topping.lower() == "end":
		action = False
		continue
	print(topping + " is added to your pizza.")