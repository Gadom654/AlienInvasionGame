with open("answers.txt","a") as new1:
	while True:
		name=input("Why you like programming?\n")
		if name=="end":
			break
		name = name + "\n"
		new1.write(name)