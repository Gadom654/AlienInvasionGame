def city_country(city,country):
	"""Returning city and country formatted together"""
	return(city.title() + ", "+country.title())
print(city_country("Warsaw","Poland"))
print(city_country("Praga","Czech Republic"))
print(city_country("Amsterdam","Netherland"))