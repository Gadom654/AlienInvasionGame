class Restaurant():
	"""docstring for Restaurant"""
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0
	def describe_restaurant(self):
		print("Restaurant name: ",self.restaurant_name ,
			"\nCuisine type:" , self.cuisine_type)
	def open_restaurant(self):
		print("Restaurant is working from 8AM to 10PM")
	def set_number_served(self,value):
		self.number_served = value
	def increment_number_served(self):
		self.number_served = self.number_served + 1
Sushi = Restaurant("Sushi bar","Korean")
Sushi.describe_restaurant()
Sushi.open_restaurant()
print(Sushi.number_served)
Sushi.number_served = 10
print(Sushi.number_served)
Sushi.set_number_served(20)
print(Sushi.number_served)
Sushi.set_number_served(30)
print(Sushi.number_served)
Sushi.increment_number_served()
Sushi.increment_number_served()
Sushi.increment_number_served()
Sushi.increment_number_served()
Sushi.increment_number_served()
print(Sushi.number_served)