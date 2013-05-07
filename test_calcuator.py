from calculator import *

import unittest

class MyTestCase(unittest.TestCase):
	def test_add(self):
		self.assertEqual(add(2,3),5)
	def test_subtract(self):
		self.assertEqual(subtract(2,3),-1)
	def test_multiply(self):
		self.assertEqual(multiply(2,3),6)
	def test_divide(self):
		self.assertEqual(divide(5,3),2)



if __name__ == "__main__":
	unittest.main(exit=False)