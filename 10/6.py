try:
	x = int(input("First number:"))
except ValueError:
	print("It has to be a number!")
try:
	y = int(input("Second number:"))
except ValueError:
	print("It has to be a number!")
z = x + y
print(z)