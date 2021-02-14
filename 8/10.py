def show_magicians(magicians):
	for magician in magicians:
		print(magician)
def make_great(magicians):
	for magician in magicians:
		great_magicians.append("Great "+ magician)
magicians = ["Maciej","Lukasz","Rafon"]
great_magicians = []
make_great(magicians)
show_magicians(great_magicians)
