import telebot
from telebot import types
import math
import config
import dbworker

# Создание бота
bot = telebot.TeleBot(config.TOKEN)


def isfloat(element):
	try:
		float(element)
	except ValueError:
		return False
	else:
		return True


# Начало диалога
@bot.message_handler(commands=['start'])
def cmd_start(message):
	bot.send_message(message.chat.id, 'Я умею выполнять действия над двумя числами!')
	dbworker.set(dbworker.make_key(message.chat.id, config.CURRENT_STATE), config.States.STATE_OPERATION.value)
	markup = types.ReplyKeyboardMarkup(row_width=2)
	itembtn1 = types.KeyboardButton('степень (a^b)')
	itembtn2 = types.KeyboardButton('логарифм (logb(a))')
	markup.add(itembtn1, itembtn2)
	bot.send_message(message.chat.id, 'Выберите пожалуйста действие', reply_markup=markup)


# По команде /reset будем сбрасывать состояния, возвращаясь к началу диалога
@bot.message_handler(commands=['reset'])
def cmd_reset(message):
	bot.send_message(message.chat.id, 'Сбрасываем результаты предыдущего ввода.')
	dbworker.set(dbworker.make_key(message.chat.id, config.CURRENT_STATE), config.States.STATE_OPERATION.value)
	markup = types.ReplyKeyboardMarkup(row_width=2)
	itembtn1 = types.KeyboardButton('степень (a^b)')
	itembtn2 = types.KeyboardButton('логарифм (logb(a))')
	markup.add(itembtn1, itembtn2)
	bot.send_message(message.chat.id, 'Выберите пожалуйста действие', reply_markup=markup)


# Выбор действия
@bot.message_handler(func=lambda message: dbworker.get(
	dbworker.make_key(message.chat.id, config.CURRENT_STATE)) == config.States.STATE_OPERATION.value)
def operation(message):
	# Текущее действие
	op = message.text
	# Сохраняем операцию
	dbworker.set(dbworker.make_key(message.chat.id, config.States.STATE_OPERATION.value), op)

	# Меняем текущее состояние
	dbworker.set(dbworker.make_key(message.chat.id, config.CURRENT_STATE), config.States.STATE_FIRST_NUM.value)
	if isinstance(message, telebot.types.Message):
		# Выводим сообщение
		bot.send_message(message.chat.id, 'Введите первое число')


# Обработка первого числа
@bot.message_handler(func=lambda message: dbworker.get(
	dbworker.make_key(message.chat.id, config.CURRENT_STATE)) == config.States.STATE_FIRST_NUM.value)
def first_num(message):
	text = message.text
	if not isfloat(text):
		# Состояние не изменяется, выводится сообщение об ошибке
		bot.send_message(message.chat.id, 'Пожалуйста введите число!')
		return
	else:
		if isinstance(message, telebot.types.Message):
			bot.send_message(message.chat.id, f'Вы ввели первое число {text}')
		# Меняем текущее состояние
		dbworker.set(dbworker.make_key(message.chat.id, config.CURRENT_STATE), config.States.STATE_SECOND_NUM.value)
		# Сохраняем первое число
		dbworker.set(dbworker.make_key(message.chat.id, config.States.STATE_FIRST_NUM.value), text)
		if isinstance(message, telebot.types.Message):
			bot.send_message(message.chat.id, 'Введите второе число')


# Обработка второго числа
@bot.message_handler(func=lambda message: dbworker.get(
	dbworker.make_key(message.chat.id, config.CURRENT_STATE)) == config.States.STATE_SECOND_NUM.value)
def second_num(message):
	text = message.text
	if not isfloat(text):
		# Состояние не изменяется, выводится сообщение об ошибке
		bot.send_message(message.chat.id, 'Пожалуйста введите число!')
		return
	else:
		if isinstance(message, telebot.types.Message):
			bot.send_message(message.chat.id, f'Вы ввели второе число {text}')
		# Сохраняем второе число
		dbworker.set(dbworker.make_key(message.chat.id, config.States.STATE_SECOND_NUM.value), text)

		# Читаем операнды из базы данных
		a = float(dbworker.get(dbworker.make_key(message.chat.id, config.States.STATE_FIRST_NUM.value)))
		b = float(dbworker.get(dbworker.make_key(message.chat.id, config.States.STATE_SECOND_NUM.value)))
		op = dbworker.get(dbworker.make_key(message.chat.id, config.States.STATE_OPERATION.value))
		markup = types.ReplyKeyboardRemove(selective=False)
		# Выполняем действие
		res = 0.0
		if op == 'степень (a^b)':
			res = a ** b
			if isinstance(message, telebot.types.Message):
				# Выводим результат
				bot.send_message(message.chat.id, f'Результат: {str(a)}^{str(b)}={str(res)}', reply_markup=markup)
			result = res
		else:
			res = math.log(a, b)
			if isinstance(message, telebot.types.Message):
				# Выводим результат
				bot.send_message(message.chat.id, f'Результат: log{str(b)}({str(a)})={str(res)}', reply_markup=markup)
			result = res

		# Меняем текущее состояние
		dbworker.set(dbworker.make_key(message.chat.id, config.CURRENT_STATE), config.States.STATE_OPERATION.value)
		markup = types.ReplyKeyboardMarkup(row_width=2)
		itembtn1 = types.KeyboardButton('степень (a^b)')
		itembtn2 = types.KeyboardButton('логарифм (logb(a))')
		markup.add(itembtn1, itembtn2)
		if isinstance(message, telebot.types.Message):
			bot.send_message(message.chat.id, 'Выберите пожалуйста действие', reply_markup=markup)
		return result


if __name__ == '__main__':
	bot.infinity_polling()
