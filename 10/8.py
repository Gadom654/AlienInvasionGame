file = "cats.txt"
try:
	with open(file) as f:
		contents = f.read()
except FileNotFoundError:
	print("This file doesn't exists.")
else:
	print(contents)
file = "dogs.txt"
try:
	with open(file) as f:
		contents = f.read()
except FileNotFoundError:
	print("This file doesn't exists.")
else:
	print(contents)
	
