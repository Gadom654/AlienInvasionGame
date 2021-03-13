with open("names.txt","w") as new1:
	while True:
		name=input("Tell me your name!\n")
		if name=="end":
			break
		print("HI",name,"!")
		name = name + "\n"
		new1.write(name)