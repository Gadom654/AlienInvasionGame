def make_album(name,album_title,track_number=""):
	"""Pushing information about album into dictionary"""
	if track_number:
		album = {"Name:" : name, "Album title:" : album_title,
		"Track number:":track_number}
	else:
		album = {"Name:" : name, "Album title:" : album_title}
	return(album)
print(make_album("Peja","Fuck TEDE"))
print(make_album("MOBBYN","MOBBYNATORMIXTAPE.COM"))
print(make_album("PR0BL3M","Art Brut"))
print(make_album("PR0BL3M","C30-C39",10))