def show_magicians(magicians):
	for magician in magicians:
		print(magician)
def make_great(magicians):
	great_magicians = []
	for magician in magicians:
		great_magicians.append("Great "+ magician)
	return great_magicians