def town_country(town,country,population=""):
	if population:
		town_name =	town.title() + ", " + country.title() + \
		 " - population " + population
	else:	
		town_name = town.title() + ", " + country.title()
	return town_name