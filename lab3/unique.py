from gen_random import gen_random


# Итератор для удаления дубликатов
class Unique(object):
	def __init__(self, items, *, ignore_case=False):
		self.used_elements = set()
		if ignore_case:
			self.data = []
			for i, item in enumerate(items):
				self.data.append(items[i].lower())
		else:
			self.data = items
		self.index = 0

	def __next__(self):
		# Нужно реализовать __next__
		while True:
			if self.index >= len(self.data):
				raise StopIteration
			else:
				current = self.data[self.index]
				self.index = self.index + 1
				if current not in self.used_elements:
					# Добавление в множество производится
					# с помощью метода add
					self.used_elements.add(current)
					return current

	def __iter__(self):
		return self

def GetUnique(items, *, ignore_case=False):
	res = []
	for i in Unique(items, ignore_case=ignore_case):
		res.append(i)
	return res

if __name__ == '__main__':
	data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
	for i in Unique(data):
		print(i, end=' ')
	print()
	data = gen_random(10, 1, 3)
	for i in Unique(data):
		print(i, end=' ')
	print()
	data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
	for i in Unique(data):
		print(i, end=' ')
	print()
	for i in Unique(data, ignore_case=True):
		print(i, end=' ')
