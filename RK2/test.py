import unittest
import main

class MainTests(unittest.TestCase):

	def test_equal_1(self):
		self.assertEqual(main.task1(), [('№1182 (детская)', 'Хоббит, или Туда и Обратно'),
										('№1182 (детская)', 'Дети синего фламинго'),
										('№206 (детская)', 'Над пропастью во ржи'), ('№206 (детская)', 'Басни Крылова'),
										('№206 (детская)', '20000 лье под водой')])

	def test_equal_2(self):
		self.assertEqual(main.task2(), [('№437', 1300.0), ('№106', 992.0), ('№101', 672.0), ('№206 (детская)', 253.67),
										('№1182 (детская)', 246.0), ('№549', 240.0)])

	def test_equal_3(self):
		self.assertEqual(main.task3(),
						 {'Басни Крылова': ['№1182 (детская)'], 'Бойцовский клуб': ['№101', '№437', '№549'],
						  'Богатый папа, бедный папа': ['№101', '№549']})


if __name__ == "__main__":
	unittest.main(verbosity=2)
