class Employee(object):
	"""docstring for Employee"""
	def __init__(self, Name, Surname, YearlySalary):
		super(Employee, self).__init__()
		self.Name = Name
		self.Surname = Surname
		self.YearlySalary = YearlySalary 
	def give_raise(self,payRaise=5000):
		self.YearlySalary = self.YearlySalary + payRaise
Marcin = Employee("Marcin","Wójcik",500000)
Marcin.give_raise(20000)
print(Marcin.YearlySalary)
