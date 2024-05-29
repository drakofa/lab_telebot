import telebot
from telebot import types

# Замените на токен вашего бота
bot = telebot.TeleBot("7478747773:AAGU_nb5DwT_U-jpNO3JnNOMR6oOSS1sOms")

# Глобальные переменные
n = 0
m = 0
d = 0

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привет! Введите любой текст:")

# Обработчик всех остальных текстовых сообщений
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    global n, m, d  # Используем глобальные переменные

    # Получение текста, введенного пользователем
    user_text = message.text

    # Логика для изменения n, m, d
    if user_text == "А":
        n += 1
    elif user_text == "Б":
        m += 1
    elif user_text == "В":
        d += 1

    # Отправка текста и значений n, m, d обратно пользователю
    bot.send_message(message.chat.id, f"Вы ввели: {user_text}\nА: {n}, Б: {m}, В: {d}")

    # Создание клавиатуры с кнопками
    markup = types.ReplyKeyboardMarkup(row_width=3)
    btn1 = types.KeyboardButton('А')
    btn2 = types.KeyboardButton('Б')
    btn3 = types.KeyboardButton('В')
    markup.add(btn1, btn2, btn3)

    # Отправка сообщения с клавиатурой
    bot.send_message(message.chat.id, "Выберите одну из кнопок:", reply_markup=markup)

# Запуск бота
bot.polling()
