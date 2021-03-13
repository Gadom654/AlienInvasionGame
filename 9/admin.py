from user import User
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