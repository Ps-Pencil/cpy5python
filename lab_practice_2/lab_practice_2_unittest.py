import unittest
from lab_practice_2 import *

class TestOOP(unittest.TestCase):
	def setUp(self):
		self.fulltime=FulltimeStaff("John",0,3000)
		self.parttime=ParttimeStaff("Sam",1,100,10)
	def testComputeSalary(self):
		self.assertEqual(self.fulltime.compute_salary(),3000)
		self.assertEqual(self.parttime.compute_salary(),1000)

if __name__ == '__main__':
	unittest.main(exit=False)