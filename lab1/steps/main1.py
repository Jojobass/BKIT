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


def main():
	'''
	Основная функция
	'''
	a = get_coef(1, 'Введите коэффициент А:')
	b = get_coef(2, 'Введите коэффициент B:')
	c = get_coef(3, 'Введите коэффициент C:')
	# Вычисление корней
	roots = solve(a, b, c)
	# Вывод корней
	len_roots = len(roots)
	if len_roots == 0:
		print('Нет корней')
	elif len_roots == 1:
		print('Один корень: {}'.format(roots[0]))
	elif len_roots == 2:
		print('Два корня: {} и {}'.format(roots[0], roots[1]))
	elif len_roots == 3:
		print('Три корня: {}, {} и {}'.format(roots[0], roots[1], roots[2]))
	elif len_roots == 4:
		print('Четыре корня: {}, {}, {} и {}'.format(roots[0], roots[1], roots[2], roots[3]))


# Если сценарий запущен из командной строки
if __name__ == "__main__":
	main()

# Пример запуска
# qr.py 1 0 -4
