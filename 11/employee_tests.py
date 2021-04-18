import unittest
from employee import Employee

class tests(unittest.TestCase):
	"""testing class Employee from emplotee.py"""
	def setUp(self):
		"""Setting up the first employee for tests"""
		self.Marcin = Employee("Marcin","Wójcik",500000)
	def test_give_default_raise(self):
		"""testing default pay raise"""
		self.Marcin.give_raise()
		self.assertEqual(self.Marcin.YearlySalary, 505000)
	def test_give_custom_raise(self):
		"""testing custom pay raise"""
		self.Marcin.give_raise(20000)
		self.assertEqual(self.Marcin.YearlySalary, 520000)
		
unittest.main()