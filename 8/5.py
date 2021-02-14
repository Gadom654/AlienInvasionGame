def describe_city(city,country="Poland"):
	"""Display information about city"""
	print(city.title(),"is in",country.title())
describe_city("Wroclaw")
describe_city("Warsaw")
describe_city("Moscow","Russia")