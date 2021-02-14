resaults = {}
while True:
	name = input("What's your name?\n")
	answer = input("If you could visit one place in the world ," +
	"where would you go?\n")
	resaults[name] = answer
	next_p = input("Is there anyone else to help me in my form?\n" +
	"If someone is here write yes.\n"	)
	if next_p.lower() != "yes":
		break
for n, a in resaults.items():
	print(n.title() , "would like to go to the:", a)