cities={
	'warsaw':{
		'country':'Poland',
		'population':1000000,
		'facts':"nothing special"
		},
	'cracov':{
		'country':'Poland',
		'population':100000,
		'facts':"nothing special"
		},
	'wroclaw':{
		'country':'Poland',
		'population':124314,
		'facts':"nothing special"
		}
}
for citie, v in cities.items():
	print(citie.title())
	country=v['country']
	pop=v['population']
	fact=v['facts']
	print("Country: " , country ,
	"\nPopulation: " , pop ,
	"\nFact: " , fact)
