with open("python.txt") as new1:
	newbie = new1.read()
	newbie2=newbie.replace("Python","Java")
	print(newbie2)
with open("python.txt") as new1:
	for line in new1.readlines():
		line1=line.replace("Python","Java")
		print(line1.strip())
with open("python.txt") as new1:
	newbie1 = new1.readlines()
for line in newbie1 :
	line1=line.replace("Python","Java")
	print(line1.strip())