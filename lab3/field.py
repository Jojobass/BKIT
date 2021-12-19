# Пример:
# goods = [
#    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
#    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
# ]
# field(goods, 'title') должен выдавать 'Ковер', 'Диван для отдыха'
# field(goods, 'title', 'price') должен выдавать {'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха', 'price': 5300}

def field(items, *args):
	assert len(args) > 0
	# Необходимо реализовать генератор
	for i, item in enumerate(items):
		if len(args) == 1:
			print(item[args[0]], end='')
			if i != len(items) - 1:
				print(', ', end='')
		else:
			buf = {}
			for arg in args:
				if arg in item:
					buf[arg] = item[arg]
			print(buf, end='')
			if i != len(items) - 1:
				print(', ', end='')
	print()

def field1(items, *args):
	res = []
	for i, item in enumerate(items):
		if len(args) == 1:
			res.append(item[args[0]])
	return res


if __name__ == '__main__':
	goods = [
		{'title': 'Ковер', 'price': 2000, 'color': 'green'},
		{'title': 'Диван для отдыха', 'color': 'black', 'price': 2100}
	]

	field(goods, 'title')
	field(goods, 'title', 'price', 'color')
