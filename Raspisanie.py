import telebot
from telebot import types
token = '6848492221:AAEAiSLhQ80a6JJ9h-7vGOR5THRmSguMs0E'
bot = telebot.TeleBot('6848492221:AAEAiSLhQ80a6JJ9h-7vGOR5THRmSguMs0E')
d1 = 'Пн:'
d2 = 'Вт:'
d3 = 'Ср:'
d4 = 'Чт:'
d5 = 'ПТ:'
d6 = 'Cб:'
l1 = 'Английский язык🇬🇧'
l2 = 'Русский язык🇷🇺'
l3 = 'Татарский язык🕌'
l4 = 'Литература🇷🇺📕'
l5 = 'Татарская литература🕌📗'
l6 = 'История⚱'
l7 = 'География🌍'
l8 = 'Биология☘'
l9 = 'Химия🧪'
l10 = 'Физика🧲'
l11 = 'ОБЖ🧯'
l12 = 'Физкультура⚽'
l13 = 'Техноллогия🔨'
l14 = 'Музыка🎸'
l15 = 'Алгебра🔢'
l16 = 'Геометрия📐'
l17 = 'Вероятность и статистика📊'
l18 = 'Обществознание⚖'
l19 = 'Информатика💻'
r1 = 'Разговоры о важном☝'
n1 = '1.'
n2 = '2.'
n3 = '3.'
n4 = '4.'
n5 = '5.'
n6 = '6.'
z1 = ' '
k8A = [d1, r1, n1 + l12, n2 + l2, n3 + l4, n4 + l5, n5 + l1, n6 + l6, z1, d2, n1 + l15, n2 + l1, n3 + l7, n4 + l14, n5 + l16, n6 + l4, z1, d3, n1 + l2, n2 + l12, n3 + l10, n4 + l4, n5 + l16, n6 + l9, z1, d4, n1 + l1, n2 + l6, n3 + l19, n4 + l7, n5 + l15, n6 + l13, z1, d5, n1 + l4, n2 + l15, n3 + l8, n4 + l9, n5 + l1, n6 + l18, z1, d6, n1 + l3, n2 + l8, n3 + l11, n4 + l17, n5 + l2, n6 + l10]
k8B = [d1, r1, n1 + l7, n2 + l16, n3 + l18, n4 + l2, n5 + l13, n6 + l14, z1, d2, n1 + l6, n2 + l4, n3 + l15, n4 + l3, n5 + l12, n6 + l10, z1, d3, n1 + l9, n2 + l1, n3 + l2, n4 + l4, n5 + l10, n6 + l15, z1, d4, n1 + l2, n2 + l17, n3 + l1, n4 + l6, n5 + l12, n6 + l19, z1, d5, n1 + l7, n2 + l8, n3 + l9, n4 + l1, n5 + l16, n6 + l4, z1, d6, n1 + l15, n2 + l11, n3 + l1, n4 + l5, n5 + l8, n6 + l3]
k8C = [d1, r1, n1 + l3, n2 + l14, n3 + l2, n4 + l1, n5 + l4, n6 + l15, z1, d2, n1 + l10, n2 + l16, n3 + l8, n4 + l17, n5 + l6, n6 + l18, z1, d3, n1 + l15, n2 + l15, n3 + l1, n4 + l9, n5 + l3, n6 + l12, z1, d4, n1 + l12, n2 + l19, n3 + l13, n4 + l1, n5 + l7, n6 + l7, z1, d5, n1 + l16, n2 + l10, n3 + l1, n4 + l2, n5 + l8, n6 + l9, z1, d6, n1 + l6, n2 + l3, n3 + l5, n4 + l2, n5 + l4, n6 + l11]
k9A = [d1, r1, n1 + l10, n2 + l6, n3 + l4, n4 + l8, n5 + l15, n6 + l12, z1, d2, n1 + l16, n2 + l2, n3 + l3, n4 + l7, n5 + l10, n6 + l1, z1, d3, n1 + l3, n2 + l4, n3 + l9, n4 + l15, n5 + l6, n6 + l7, z1, d4, n1 + l19, n2 + l12, n3 + l15, n4 + l4, n5 + l5, n6 + l4, z1, d5, n1 + l18, n2 + l9, n3 + l2, n4 + l17, n5 + l6, n6 + l1, z1, d6, n1 + l1, n2 + l2, n3 + l10, n4 + l11, n5 + l16, n6 + l8]
k9B = [d1, r1, n1 + l1, n2 + l18, n3 + l10, n4 + l6, n5 + l12, n6 + l7, z1, d2, n1 + l2, n2 + l3, n3 + l12, n4 + l10, n5 + l17, n6 + l5, z1, d3, n1 + l1, n2 + l3, n3 + l15, n4 + l8, n5 + l9, n6 + l10, z1, d4, n1 + l10, n2 + l3, n3 + l4, n4 + l19, n5 + l6, n6 + l5, z1, d5, n1 + l9, n2 + l16, n3 + l7, n4 + l8, n5 + l2, n6 + l4, z1, d6, n1 + l11, n2 + l15, n3 + l2, n4 + l4, n5 + l1, n6 + l16]
k9C = [d1, r1, n1 + l15, n2 + l4, n3 + l16, n4 + l10, n5 + l6, n6 + l18, z1, d2, n1 + l3, n2 + l7, n3 + l10, n4 + l1, n5 + l2, n6 + l4, z1, d3, n1 + l2, n2 + l9, n3 + l2, n4 + l10, n5 + l16, n6 + l4, z1, d4, n1 + l4, n2 + l7, n3 + l5, n4 + l10, n5 + l19, n6 + l8, z1, d5, n1 + l8, n2 + l1, n3 + l15, n4 + l6, n5 + l9, n6 + l12, z1, d6, n1 + l2, n2 + l1, n3 + l15, n4 + l17, n5 + l11, n6 + l6]
#---------------------------------------------------
d18A = [d1, r1, n1 + l12, n2 + l2, n3 + l4, n4 + l5, n5 + l1, n6 + l6]
d18B = [d1, r1, n1 + l7, n2 + l16, n3 + l18, n4 + l2, n5 + l13, n6 + l14]
d18C = [d1, r1, n1 + l3, n2 + l14, n3 + l2, n4 + l1, n5 + l4, n6 + l15]
d19A = [d1, r1, n1 + l10, n2 + l6, n3 + l4, n4 + l8, n5 + l15, n6 + l12]
d19B = [d1, r1, n1 + l1, n2 + l18, n3 + l10, n4 + l6, n5 + l12, n6 + l7]
d19C = [d1, r1, n1 + l15, n2 + l4, n3 + l16, n4 + l10, n5 + l6, n6 + l18]
#------------------------------------------
d28A = [d2, n1 + l15, n2 + l1, n3 + l7, n4 + l14, n5 + l16, n6 + l4]
d28B = [d2, n1 + l6, n2 + l4, n3 + l15, n4 + l3, n5 + l12, n6 + l10]
d28C = [d2, n1 + l10, n2 + l16, n3 + l8, n4 + l17, n5 + l6, n6 + l18]
d29A = [d2, n1 + l16, n2 + l2, n3 + l3, n4 + l7, n5 + l10, n6 + l1]
d29B = [d2, n1 + l2, n2 + l3, n3 + l12, n4 + l10, n5 + l17, n6 + l5]
d29C = [d2, n1 + l3, n2 + l7, n3 + l10, n4 + l1, n5 + l2, n6 + l4]
#------------------------------------------
d38A = [d3, n1 + l2, n2 + l12, n3 + l10, n4 + l4, n5 + l16, n6 + l9]
d38B = [d3, n1 + l9, n2 + l1, n3 + l2, n4 + l4, n5 + l10, n6 + l15]
d38C = [d3, n1 + l15, n2 + l15, n3 + l1, n4 + l9, n5 + l3, n6 + l12]
d39A = [d3, n1 + l3, n2 + l4, n3 + l9, n4 + l15, n5 + l6, n6 + l7]
d39B = [d3, n1 + l1, n2 + l3, n3 + l15, n4 + l8, n5 + l9, n6 + l10]
d39C = [d3, n1 + l2, n2 + l9, n3 + l2, n4 + l10, n5 + l16, n6 + l4]
#------------------------------------------
d48A = [d4, n1 + l1, n2 + l6, n3 + l19, n4 + l7, n5 + l15, n6 + l13]
d48B = [d4, n1 + l2, n2 + l17, n3 + l1, n4 + l6, n5 + l12, n6 + l19]
d48C = [d4, n1 + l12, n2 + l19, n3 + l13, n4 + l1, n5 + l7, n6 + l7]
d49A = [d4, n1 + l19, n2 + l12, n3 + l15, n4 + l4, n5 + l5, n6 + l4]
d49B = [d4, n1 + l10, n2 + l3, n3 + l4, n4 + l19, n5 + l6, n6 + l5]
d49C = [d4, n1 + l4, n2 + l7, n3 + l5, n4 + l10, n5 + l19, n6 + l8]
#------------------------------------------
d58A = [d5, n1 + l4, n2 + l15, n3 + l8, n4 + l9, n5 + l1, n6 + l18]
d58B = [d5, n1 + l7, n2 + l8, n3 + l9, n4 + l1, n5 + l16, n6 + l4]
d58C = [d5, n1 + l16, n2 + l10, n3 + l1, n4 + l2, n5 + l8, n6 + l9]
d59A = [d5, n1 + l18, n2 + l9, n3 + l2, n4 + l17, n5 + l6, n6 + l1]
d59B = [d5, n1 + l9, n2 + l16, n3 + l7, n4 + l8, n5 + l2, n6 + l4]
d59C = [d5, n1 + l8, n2 + l1, n3 + l15, n4 + l6, n5 + l9, n6 + l12]
#------------------------------------------
d68A = [d6, n1 + l3, n2 + l8, n3 + l11, n4 + l17, n5 + l2, n6 + l10]
d68B = [d6, n1 + l15, n2 + l11, n3 + l1, n4 + l5, n5 + l8, n6 + l3]
d68C = [d6, n1 + l6, n2 + l3, n3 + l5, n4 + l2, n5 + l4, n6 + l11]
d69A = [d6, n1 + l1, n2 + l2, n3 + l10, n4 + l11, n5 + l16, n6 + l8]
d69B = [d6, n1 + l11, n2 + l15, n3 + l2, n4 + l4, n5 + l1, n6 + l16]
d69C = [d6, n1 + l2, n2 + l1, n3 + l15, n4 + l17, n5 + l11, n6 + l6]
@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    nachl = types.KeyboardButton('➡Смотреть⬅')
    markup.add(nachl)
    bot.send_message(message.chat.id, f"👋Привет {message.from_user.first_name}! Это бот, в котором ты сможешь смотреть расписание уроков на все дни📅", reply_markup=markup)
@bot.message_handler(content_types=['text'])
def button_message(message):
    if message.text == '➡Смотреть⬅':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        eightA = types.KeyboardButton('8А')
        eightB = types.KeyboardButton('8Б')
        eightC = types.KeyboardButton('8В')
        nineA = types.KeyboardButton('9А')
        nineB = types.KeyboardButton('9Б')
        nineC = types.KeyboardButton('9В')
        markup.add(eightA, eightB, eightC, nineA, nineB, nineC)
        bot.send_message(message.chat.id, "Выбери свой класс📚", reply_markup=markup)
#8А
    if message.text == '8А':
        bot.send_message(message.chat.id, '\n'.join(k8A))
#8Б
    if message.text == '8Б':
        bot.send_message(message.chat.id, '\n'.join(k8B))
#8В
    if message.text == '8В':
        bot.send_message(message.chat.id, '\n'.join(k8C))
#9А
    if message.text == '9А':
        bot.send_message(message.chat.id, '\n'.join(k9A))
#9Б
    if message.text == '9Б':
        bot.send_message(message.chat.id, '\n'.join(k9B))
#9В
    if message.text == '9В':
        bot.send_message(message.chat.id, '\n'.join(k9C))
bot.polling(none_stop=True)