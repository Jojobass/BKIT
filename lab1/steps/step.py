# -*- coding: utf-8 -*
from behave import given, when, then
import main1


@given(r"Coefs are {a:g}, {b:g}, {c:g}")
def have_numbers(step, a, b, c):
	step.a = float(a)
	step.b = float(b)
	step.c = float(c)


@when(r"I solve the bisquare equation")
def sum_numbers(step):
	step.result = str(main1.solve(step.a, step.b, step.c))


@then(r"I expect the result to be {result}")
def expect_result(step, result):
	print(step.result)
	assert step.result == result
