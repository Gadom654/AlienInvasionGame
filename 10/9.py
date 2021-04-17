file = "cats.txt"
try:
	with open(file) as f:
		contents = f.read()
except FileNotFoundError:
	pass
else:
	print(contents)
file = "dogs.txt"
try:
	with open(file) as f:
		contents = f.read()
except FileNotFoundError:
	pass
else:
	print(contents)
	