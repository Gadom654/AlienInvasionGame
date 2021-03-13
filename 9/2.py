class Restaurant():
	"""docstring for Restaurant"""
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
	def describe_restaurant(self):
		print("Restaurant name: ",self.restaurant_name ,
			"\nCuisine type:" , self.cuisine_type)
	def open_restaurant(self):
		print("Restaurant is working from 8AM to 10PM")
Sushi = Restaurant("Sushi bar","Korean")
Sushi.describe_restaurant()
Sushi.open_restaurant()
Kebab = Restaurant("Zahir","Turkish")
Kebab.describe_restaurant()
Chicken = Restaurant("TaiPai","Chinese")
Chicken.describe_restaurant()