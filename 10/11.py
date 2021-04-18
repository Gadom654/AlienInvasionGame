import json

fav_number = int(input("Write your favourite number: "))

file = "fav_number.json"
with open(file,"w") as f:
	json.dump(fav_number,f)