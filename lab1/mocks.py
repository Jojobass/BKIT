from unittest.mock import Mock
import unittest

import sys
import math


def get_coef(index, prompt):
	'''
	Читаем коэффициент из командной строки или вводим с клавиатуры
	Args:
		index (int): Номер параметра в командной строке
		prompt (str): Приглашение для ввода коэффицента
	Returns:
		float: Коэффициент квадратного уравнения
	'''
	is_cmd_input = False
	try:
		# Пробуем прочитать коэффициент из командной строки
		coef_str = sys.argv[index]
	except:
		# Вводим с клавиатуры
		print(prompt)
		coef_str = input()
	else:
		is_cmd_input = True
	# Переводим строку в действительное число
	try:
		coef = float(coef_str)
	except:
		print('Incorrect input. Try again.')
		if is_cmd_input:
			sys.exit()
		else:
			coef = get_coef(index, prompt)
	return coef


def get_discriminant(a, b, c):
	return b ** 2 - 4 * a * c


def get_roots_squared(a, b, d):
	res = set()
	if d == 0.0:
		res.add(-b / (2.0 * a))
	if d > 0.0:
		sqrtD = math.sqrt(d)
		res.add((-b + sqrtD) / (2.0 * a))
		res.add((-b - sqrtD) / (2.0 * a))
	return res


def get_all_roots(arr):
	res = set()
	for item in arr:
		if item > 0:
			res.add(math.sqrt(item))
			res.add(-math.sqrt(item))
		elif item == 0.0:
			res.add(0.0)
	return res


def solve(a, b, c):
	'''
	Вычисление корней квадратного уравнения
	Args:
		a (float): коэффициент А
		b (float): коэффициент B
		c (float): коэффициент C
	Returns:
		list[float]: Список корней
	'''
	D = get_discriminant(a, b, c)
	roots_squared = get_roots_squared(a, b, D)
	result = list(get_all_roots(roots_squared))
	return result


d = Mock()
rs = Mock()

class Test_funcs(unittest.TestCase):
	def test_get_D(self):
		d.return_value = 9
		D = d(1, -5, 4)
		d.assert_called_once()
		self.assertEqual(D, 9)

	def test_get_roots_sqr_1(self):
		d.return_value = 9
		D = d(1, -5, 4)
		RS = get_roots_squared(1, -5, D)
		self.assertEqual(RS, {1, 4})

	def test_get_roots_sqr_2(self):
		d.return_value = 16
		D = d()
		RS = get_roots_squared(1, -6, D)
		self.assertEqual(RS, {1, 5})

	def test_all_roots_1(self):
		rs.return_value = {1, 4}
		RS = rs()
		R = get_all_roots(RS)
		self.assertEqual(R, {1, -1, 2, -2})

	def test_all_roots_2(self):
		rs.return_value = {1, 9}
		RS = rs()
		R = get_all_roots(RS)
		self.assertEqual(R, {1, -1, 3, -3})


if __name__ == '__main__':
	unittest.main(verbosity=2)

