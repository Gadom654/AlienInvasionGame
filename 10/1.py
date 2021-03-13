with open("python.txt") as new1:
	newbie = new1.read()
	print(newbie)
with open("python.txt") as new1:
	for line in new1.readlines():
		print(line.strip())
with open("python.txt") as new1:
	newbie1 = new1.readlines()
for line in newbie1 :
	print(line.strip())