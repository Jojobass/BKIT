import unittest
import main
from math import pi

class MainTests(unittest.TestCase):

	def test_D(self):
		self.assertEqual(main.get_discriminant(2*pi, 2*pi, pi/2), 0)

	def test_roots_squared_1(self):
		self.assertEqual(main.get_roots_squared(2, 4, main.get_discriminant(2, 4, 2)), {-1})
	def test_roots_squared_2(self):
		self.assertEqual(main.get_roots_squared(2, -4, main.get_discriminant(2, -4, 2)), {1})
	def test_roots_squared_3(self):
		self.assertEqual(main.get_roots_squared(1, -1, main.get_discriminant(1, -1, 0)), {0, 1})
	def test_roots_squared_4(self):
		self.assertEqual(main.get_roots_squared(1, 0, main.get_discriminant(1, 0, 0)), {0})

	def test_roots_1(self):
		self.assertEqual(main.solve(2, 4, 2), [])
	def test_roots_2(self):
		self.assertEqual(main.solve(1, 0, 0), [0])
	def test_roots_3(self):
		self.assertEqual(main.solve(2, -4, 2), [1, -1])
	def test_roots_4(self):
		self.assertEqual(main.solve(1, -1, 0), [0, 1, -1])
	def test_roots_5(self):
		self.assertEqual(main.solve(1, -5, 4), [1, 2, -1, -2])




if __name__ == "__main__":
	unittest.main(verbosity=2)