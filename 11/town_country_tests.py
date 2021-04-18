import unittest
from town_country import town_country

class tests(unittest.TestCase):
	"""testing class"""
	def test_town_country(self):
		"""testing town_country function"""
		testedValue = town_country("wrocław","polska")
		self.assertEqual(testedValue, "Wrocław, Polska")
		
	def test_pop(self):
		"""is population working correct in town_country function"""
		testedValue = town_country("wrocław","polska","5000000")
		self.assertEqual(testedValue,"Wrocław, Polska - population 5000000")
unittest.main()