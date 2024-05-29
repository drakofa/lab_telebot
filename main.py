import telebot
from telebot import types

# Замените на токен вашего бота
bot = telebot.TeleBot("7478747773:AAGU_nb5DwT_U-jpNO3JnNOMR6oOSS1sOms")

questions = [
    ("Выбирая свою гильдию, что для тебя важнее: творческий процесс, технические навыки или бизнес-стратегия?",
     ["А: Творческий процесс 🎨", "Б: Технические навыки 💻", "В: Бизнес-стратегия 📈"]),
    (
    "Какой аспект информационных технологий тебе интереснее всего: визуальное представление данных, знание языков программирования или оптимизация бизнес-процессов?",
    ["А: Визуальное представление данных 📊", "Б: Языки программирования 💬", "В: Оптимизация бизнес-процессов 🔄"]),
    (
    "Представь, что ты можешь создать свою цифровую магию: какие способности бы ты выбрал: создание виртуальных миров, взлом информационных систем или разработку умных решений для бизнеса?",
    ["А: Создание виртуальных миров 🌐", "Б: Взлом информационных систем 🔓",
     "В: Разработка умных решений для бизнеса 💼"]),
    ("Какой стиль игры тебе ближе: стратегия и планирование, технические испытания или творческие задания?",
     ["А: Стратегия и планирование 📝", "Б: Технические испытания 🔧", "В: Творческие задания 🎭"]),
    (
    "Что бы ты выбрал для решения сложной задачи: коллективное творчество, индивидуальные технические навыки или аналитический подход?",
    ["А: Коллективное творчество 🤝", "Б: Индивидуальные технические навыки 💡", "В: Аналитический подход 🧩"]),
    (
    "Если тебе предстоит создать новый проект, что ты выберешь: уникальный дизайн и визуальное привлечение, безупречная функциональность или экономическая эффективность?",
    ["А: Уникальный дизайн и визуальное привлечение 🎨", "Б: Безупречная функциональность ⚙️",
     "В: Экономическая эффективность 💰"]),
    (
    "Что важнее для тебя в процессе обучения: теоретические знания, практические навыки или возможность экспериментировать и творить?",
    ["А: Теоретические знания 📚", "Б: Практические навыки 🛠️", "В: Экспериментирование и творчество 🌈"]),
    (
    "Представь, что у тебя есть магический артефакт: он может обеспечить тебе одно из следующего - мгновенное понимание любого кода, невидимость в цифровом пространстве или способность прогнозировать технологические тренды. Какой эффект ты бы выбрал?",
    ["А: Мгновенное понимание любого кода 🧙", "Б: Невидимость в цифровом пространстве 🕵️‍♂️",
     "В: Способность прогнозировать технологические тренды 🔮"])
]

current_question = {}
answers_count = {
    "А": 0,
    "Б": 0,
    "В": 0
}


# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.chat.id
    current_question[user_id] = 0
    send_question(message)


def send_question(message):
    user_id = message.chat.id
    if user_id in current_question:
        question_index = current_question[user_id]
        if question_index < len(questions):
            question_text, options = questions[question_index]
            markup = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
            for option in options:
                markup.add(types.KeyboardButton(option))
            bot.send_message(user_id, question_text, reply_markup=markup)
        else:
            send_results(message)
            del current_question[user_id]


def record_answer(answer):
    if answer.startswith("А"):
        answers_count["А"] += 1
    elif answer.startswith("Б"):
        answers_count["Б"] += 1
    elif answer.startswith("В"):
        answers_count["В"] += 1


def send_results(message):
    a_count = answers_count["А"]
    b_count = answers_count["Б"]
    c_count = answers_count["В"]

    if a_count > b_count and a_count > c_count:
        results = (
            f"Ты прошёл весь тест, и по моим данным, я могу сказать что тебе стоит идти в гильдию ИнфоМедию\n"
        )
    elif b_count > a_count and b_count > c_count:
        results = (
            f"Опрос пройден, и по моим видениям, я могу предположить, что тебе стоит пойти в гильдию КодМастерс\n"
        )
    elif c_count > a_count and c_count > b_count:
        results = (
            f"Ты прошел испытание, и что-то мне подсказывает, что ты полностью раскроешь свой потенциал в гильдии БизнесИнноваторс\n"
        )
    elif a_count == b_count and a_count > c_count:
        results = (
            f"Твои навыки мне подсказывают что ты хорош в дизайне и программировании, думаю что тебе самому можно доверить выбор между двумя гильдиями: ИнфоМедия и КодМастерс\n"
        )
    elif b_count == c_count and b_count > a_count:
        results = (
            f"А ты не плох, как я вижу, ты хорош в двух аспектах: в программировании и в бизнес решениях\n"
        )
    elif a_count == b_count == c_count:
        results = (
            f"Ну ты прям не могу, по моим догадкам тебе надо идти фулстак разработчиком, желаю тебе удачи\n"
        )

    bot.send_message(message.chat.id, results)


# Обработчик всех текстовых сообщений
@bot.message_handler(func=lambda message: True)
def handle_answer(message):
    user_id = message.chat.id
    if user_id in current_question:
        record_answer(message.text)
        current_question[user_id] += 1
        send_question(message)
    else:
        bot.send_message(user_id, "Введите команду /start, чтобы начать заново.")


# Запуск бота
bot.polling()
