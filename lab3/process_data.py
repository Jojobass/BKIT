import json
import random
import sys
from unique import GetUnique
from field import field1
from print_result import print_result
from cm_timer import cm_timer_1

# Сделаем другие необходимые импорты

path = './data_light.json'

# Необходимо в переменную path сохранить путь к файлу, который был передан при запуске сценария

with open(path, encoding='utf8') as f:
	data = json.load(f)


# Далее необходимо реализовать все функции по заданию, заменив `raise NotImplemented`
# Предполагается, что функции f1, f2, f3 будут реализованы в одну строку
# В реализации функции f4 может быть до 3 строк

@print_result
def f1(arg):
	return GetUnique(field1(arg, 'job-name'), ignore_case=True)


# f1(data)


@print_result
def f2(arg):
	return list(filter(lambda x: x.split()[0] == 'программист', arg))


# f2(f1(data))

@print_result
def f3(arg):
	return list(map(lambda x: x + ' c опытом Python', arg))


# f3(f2(f1(data)))

@print_result
def f4(arg):
	return [x + f', зарплата {y} руб.' for x, y in zip(arg, [random.randint(100000, 200000) for i in range(len(arg))])]


if __name__ == '__main__':
	with cm_timer_1():
		f4(f3(f2(f1(data))))
