import  telebot
from telebot import types
bot = telebot.TeleBot("7478747773:AAGU_nb5DwT_U-jpNO3JnNOMR6oOSS1sOms")


# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привет! Введите любой текст:")

# Обработчик всех остальных текстовых сообщений
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    # Получение текста, введенного пользователем
    user_text = message.text

    # Отправка текста обратно пользователю
    bot.send_message(message.chat.id, f"Вы ввели: {user_text}")

    # Создание клавиатуры с кнопками
    markup = types.ReplyKeyboardMarkup(row_width=2)
    btn1 = types.KeyboardButton('Кнопка 1')
    btn2 = types.KeyboardButton('Кнопка 2')
    markup.add(btn1, btn2)

    # Отправка сообщения с клавиатурой
    bot.send_message(message.chat.id, "Выберите одну из кнопок:", reply_markup=markup)

# Запуск бота
bot.polling()

