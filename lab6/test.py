import bot
import unittest


class chat:
	def __init__(self):
		self.id = 0


class mes:
	def __init__(self, text_):
		self.text = text_
		self.chat = chat()


class Test_bot(unittest.TestCase):
	def test_power_1(self):
		bot.operation(mes("степень (a^b)"))
		bot.first_num(mes("6"))
		res = bot.second_num(mes("3"))

		self.assertEqual(res, 216)

	def test_power_2(self):
		bot.operation(mes("степень (a^b)"))
		bot.first_num(mes("9"))
		res = bot.second_num(mes("0.5"))

		self.assertEqual(res, 3)

	def test_log_1(self):
		bot.operation(mes("логарифм (logb(a))"))
		bot.first_num(mes("9"))
		res = bot.second_num(mes("3"))

		self.assertEqual(res, 2)

	def test_log_2(self):
		bot.operation(mes("логарифм (logb(a))"))
		bot.first_num(mes("9"))
		res = bot.second_num(mes("81"))

		self.assertEqual(res, 0.5)


if __name__ == "__main__":
	unittest.main(verbosity=2)
