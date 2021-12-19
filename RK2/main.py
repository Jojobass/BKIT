class Book:
	def __init__(self, _id, name, num_of_pages, lib_id):
		self.id = _id
		self.name = name
		self.num_of_pages = num_of_pages
		self.lib_id = lib_id


class Library:
	"""Отдел"""

	def __init__(self, _id, name):
		self.id = _id
		self.name = name


class BookLibrary:
	"""
	'Сотрудники отдела' для реализации
	связи многие-ко-многим
	"""

	def __init__(self, lib_id, book_id):
		self.lib_id = lib_id
		self.book_id = book_id


# Отделы
libraries = [
	Library(1, '№101'),
	Library(2, '№106'),
	Library(3, '№1182 (детская)'),
	Library(4, '№437'),
	Library(5, '№206 (детская)'),
	Library(6, '№549')
]

# Сотрудники
books = [
	Book(1, 'Улисс', 992, 2),
	Book(2, 'Над пропастью во ржи', 213, 5),
	Book(3, 'Преступление и наказание', 672, 1),
	Book(4, 'Басни Крылова', 100, 5),
	Book(5, 'Война и Мир', 1300, 4),
	Book(6, 'Хоббит, или Туда и Обратно', 268, 3),
	Book(7, 'Бойцовский клуб', 256, 6),
	Book(8, 'Дети синего фламинго', 224, 3),
	Book(9, 'Богатый папа, бедный папа', 224, 6),
	Book(10, '20000 лье под водой', 448, 5)
]
# связь 'многие ко многим'
books_libraries = [
	BookLibrary(1, 1),
	BookLibrary(1, 3),
	BookLibrary(1, 5),
	BookLibrary(1, 7),
	BookLibrary(1, 9),
	BookLibrary(2, 2),
	BookLibrary(2, 3),
	BookLibrary(2, 6),
	BookLibrary(2, 10),
	BookLibrary(3, 4),
	BookLibrary(3, 6),
	BookLibrary(3, 8),
	BookLibrary(4, 1),
	BookLibrary(4, 2),
	BookLibrary(4, 3),
	BookLibrary(4, 7),
	BookLibrary(5, 3),
	BookLibrary(5, 5),
	BookLibrary(5, 6),
	BookLibrary(5, 10),
	BookLibrary(6, 7),
	BookLibrary(6, 9)
]


def main():
	"""Основная функция"""

	# Соединение данных один-ко-многим
	one_to_many = [(book.name, book.num_of_pages, lib.name)
				   for lib in libraries
				   for book in books
				   if book.lib_id == lib.id]

	# Соединение данных многие-ко-многим
	many_to_many_temp = [(lib.name, bl.lib_id, bl.book_id)
						 for lib in libraries
						 for bl in books_libraries
						 if lib.id == bl.lib_id]

	many_to_many = [(book.name, book.num_of_pages, lib_name)
					for lib_name, lib_id, book_id in many_to_many_temp
					for book in books if book.id == book_id]

	print('Задание А1')
	res1 = []
	for book_name, book_num, lib_name in one_to_many:
		if '(детская)' in lib_name:
			res1.append((lib_name, book_name))
	print(res1)

	print('\nЗадание А2')
	dict2 = {}
	for lib in libraries:
		dict2[lib.name] = [0, 0]
	# перебираем библиотеки
	for lib in libraries:
		# перебираем записи соответствия книги и библиотеки
		for i in one_to_many:
			if i[2] == lib.name:
				# добавляем количество страниц книги в общую сумму страниц в библиотеке
				dict2[lib.name][0] += i[1]
				# увеличиваем количество книг в библиотеке
				dict2[lib.name][1] += 1
	print(dict2)
	res2 = []
	# делаем список библиотек и среднего числа страниц в книге в библиотеке
	for key, value in dict2.items():
		res2.append((key, round(value[0] / value[1], 2)))
	# сортируем по числу страниц
	res2 = sorted(res2, key=lambda av: av[1], reverse=True)
	print(res2)

	print('\nЗадание А3')
	res3 = {}
	# создаем список для библиотек для книг с первой "Б"
	for book in books:
		if book.name[0] == 'Б':
			res3[book.name] = []

	# перебираем записи соответствия книг и библиотек
	for i in many_to_many:
		# если книга подходит
		if i[0][0] == 'Б':
			# записываем библиотеку в список библиотек, в которых есть эта книга
			res3[i[0]].append(i[2])
	print(res3)


if __name__ == '__main__':
	main()
