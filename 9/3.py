class User(object):
	"""docstring for User"""
	def __init__(self, first_name, last_name, age, email):
		super(User, self).__init__()
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.email = email
	def describe_user(self):
		print("First name:", self.first_name,
			"\nLast name:", self.last_name,
			"\nAge:", self.age,
			"\nEmail:", self.email)
		pass
	def greet_user(self):
		print("Hi,", self.first_name , "you'r welcome.")
Luki = User("Luki","Kwiatkowski","20","luki69@gmail.com")
Marcin = User("Marcin","Kwiatkowski","20","luki69@gmail.com")
Artur = User("Artur","Kwiatkowski","20","luki69@gmail.com")
Luki.describe_user()
Marcin.describe_user()
Artur.describe_user()
Luki.greet_user()
Marcin.greet_user()
Artur.greet_user()