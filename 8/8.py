def make_album(name,album_title,track_number=""):
	"""Pushing information about album into dictionary"""
	if track_number:
		album = {"Name:" : name, "Album title:" : album_title,
		"Track number:":track_number}
	else:
		album = {"Name:" : name, "Album title:" : album_title}
	return(album)
while True:
	nex = input("Do you want to add new album, if not press n")
	if(nex=="n"):
		break
	names = input("Write name of artist: ")
	album_titles = input("Write title of album: ")
	track_numbers = input("Write track number on album: ")
	print(make_album(names,album_titles,track_numbers))
print(make_album("Peja","Fuck TEDE"))
print(make_album("MOBBYN","MOBBYNATORMIXTAPE.COM"))
print(make_album("PR0BL3M","Art Brut"))
print(make_album("PR0BL3M","C30-C39",10))
