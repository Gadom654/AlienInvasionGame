class User():
	"""docstring for User"""
	def __init__(self, first_name, last_name, age, email):
		super(User, self).__init__()
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.email = email
		self.login_attempts = 0
	def describe_user(self):
		print("First name:", self.first_name,
			"\nLast name:", self.last_name,
			"\nAge:", self.age,
			"\nEmail:", self.email)
		pass
	def greet_user(self):
		print("Hi,", self.first_name , "you'r welcome.")
	def increment_login_attempts(self):
		self.login_attempts = self.login_attempts + 1
	def reset_login_attempts(self):
		self.login_attempts = 0
class Admin(User):
	"""docstring for Admin"""
	def __init__(self, first_name, last_name, age, email):
		super().__init__(first_name, last_name, age, email)
		self.privileges = Privileges()
class Privileges():
	"""docstring for Privileges"""
	def __init__(self):
		self.privileges = ["You can add post","You can modify your post",
		"You can delete your post","you can ban users"]
	def show_privilelges(self):
		for x in self.privileges:
			print(x)