import os
import telebot
from telebot import types

# Токен бота
TOKEN = '5025597859:AAEWXRIIXFHWLeC7kCZThTzokzZigK2d2Uc'

# Сообщения
mes_pairs = 'пары'
mes_exams = 'экзамены'

# Путь к текущему каталогу
cur_path = os.path.dirname(os.path.abspath(__file__))

# Создание бота
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
	# Идентификатор диалога
	chat_id = message.chat.id

	# Текст, введенный пользователем, то есть текст с кнопки
	text = message.text

	# Проверка сообщения и вывод данных
	if text == mes_pairs:
		img = open(os.path.join(cur_path, 'img\pairs.jpeg'), 'rb')
		bot.send_photo(chat_id, img)
	elif text == mes_exams:
		img = open(os.path.join(cur_path, 'img\exams.jpeg'), 'rb')
		bot.send_photo(chat_id, img)
	else:
		markup = types.ReplyKeyboardMarkup(row_width=2)
		itembtn1 = types.KeyboardButton(mes_pairs)
		itembtn2 = types.KeyboardButton(mes_exams)
		markup.add(itembtn1, itembtn2)
		bot.send_message(chat_id, 'Пожалуйста, нажмите кнопку', reply_markup=markup)

# @bot.message_handler(commands=[mes_pairs])
# def send_pairs(message):
# 	# Идентификатор диалога
# 	chat_id = message.chat.id
# 	img = open(os.path.join(cur_path, 'img\pairs.jpeg'), 'rb')
# 	bot.send_photo(chat_id, img)
#
#
# @bot.message_handler(commands=[mes_exams])
# def send_pairs(message):
# 	# Идентификатор диалога
# 	chat_id = message.chat.id
# 	img = open(os.path.join(cur_path, 'img\exams.jpeg'), 'rb')
# 	bot.send_photo(chat_id, img)
#
# @bot.message_handler(func=lambda mes: mes.text == None or (mes.text != mes_pairs and mes.text != mes_exams))
# def wait(message):
# 	# Идентификатор диалога
# 	chat_id = message.chat.id
# 	markup = types.ReplyKeyboardMarkup(row_width=2)
# 	itembtn1 = types.KeyboardButton(mes_pairs)
# 	itembtn2 = types.KeyboardButton(mes_exams)
# 	markup.add(itembtn1, itembtn2)
# 	bot.send_message(chat_id, 'Пожалуйста, нажмите кнопку', reply_markup=markup)




bot.infinity_polling()
