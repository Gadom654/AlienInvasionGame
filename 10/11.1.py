import json

file = "fav_number.json"
with open(file) as f:
	fav_number = json.load(f)
print("I know your favourite number, it's", fav_number)