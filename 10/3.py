answer= input("Tell me your name:")
with open("name.txt","w") as new1:
	new1.write(answer)