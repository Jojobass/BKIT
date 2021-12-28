# -*- coding: utf-8 -*
from behave import given, when, then
import bot

class chat:
	def __init__(self):
		self.id = 0


class mes:
	def __init__(self, text_):
		self.text = text_
		self.chat = chat()

@given(r"I choose {operation}, {a}, {b}")
def have_numbers(step, operation, a, b):
	if operation == 'log':
		op = mes('логарифм (logb(a))')
	else:
		op = mes('степень (a^b)')
	bot.operation(op)
	bot.first_num(mes(a))
	step.second_num = mes(b)



@when(r"I perform the operation")
def sum_numbers(step):
	step.result = str(bot.second_num(step.second_num))


@then(r"I expect the result to be {result}")
def expect_result(step, result):
	assert step.result == result
