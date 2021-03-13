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
class IceCreamStand(Restaurant):
	"""docstring for IceCreamStand"""
	def __init__(self, restaurant_name, cuisine_type):
		super().__init__(restaurant_name, cuisine_type)
		self.flavors = ["Chocolate","strawbarry","kiwi","lion"]
	def show_flavors(self):
		print(self.flavors)