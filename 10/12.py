import json

file = "fav_number.json"
try:
	with open(file) as f:
		fav_number = json.load(f)
except FileNotFoundError:
	fav_number = int(input("Write your favourite number: "))
	with open(file,"w") as f:
		json.dump(fav_number,f)
else:
	print("I know your favourite number, it's", fav_number)
