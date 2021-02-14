def make_car(name,model,**others):
	car = {}
	car["Name"] = name.title()
	car["Model"] = model.title()
	for k,v in others.items():
		car[k]=v
	return car
car = make_car("subaru","outback",color="black",tow_package=True)
print(car)