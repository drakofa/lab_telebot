import telebot
from telebot import types

# Замените на токен вашего бота
bot = telebot.TeleBot("7478747773:AAGU_nb5DwT_U-jpNO3JnNOMR6oOSS1sOms")

# Глобальная переменная
n = 0

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привет! Введите любой текст:")

# Обработчик всех остальных текстовых сообщений
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    global n  # Используем глобальную переменную n

    # Получение текста, введенного пользователем
    user_text = message.text

    # Логика для изменения n
    if user_text == "a1":
        n += 1
    elif user_text == "a2":
        n -= 1

    # Отправка текста и значения n обратно пользователю
    bot.send_message(message.chat.id, f"Вы ввели: {user_text}\nТекущее значение n: {n}")

    # Создание клавиатуры с кнопками
    markup = types.ReplyKeyboardMarkup(row_width=2)
    btn1 = types.KeyboardButton('a1')
    btn2 = types.KeyboardButton('a2')
    markup.add(btn1, btn2)

    # Отправка сообщения с клавиатурой
    bot.send_message(message.chat.id, "Выберите одну из кнопок:", reply_markup=markup)

# Запуск бота
bot.polling()
