import telebot

#telebot.apihelper.proxy = {'https': 'https://51.158.111.229:8811'}

bot = telebot.TeleBot('807872124:AAE584RSfGzekXBOF84j1309iNUXE74L7Yg')

place = 'Компания \"Pernod ricard\"\n'\
        '+7 (778) 471-08-80\n' \
        'Игорь'
place2 = 'Компания «Pernod Ricard»\n'\
         '+7 (777) 450-82-55\n'\
         'Леонид'

p = [place, place2]

cities = ['Нур-Султан', 'Павлодар']
cities_low = []

for i in cities:
    cities_low.append(i.lower())

alco = ['Jameson', 'Сhivas','Absolut','Olmeca','Beefeather','Ballantine\'s']
alco_low = []

for i in alco:
    alco_low.append(i.lower())

keyboard1 = telebot.types.ReplyKeyboardMarkup()


@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard1.keyboard.clear()
    for i in cities:
        keyboard1.row(i)
    bot.send_message(message.chat.id, 'Где вы находитесь?', reply_markup=keyboard1)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() in cities_low:
        a = p[cities_low.index(a)]
        keyboard1.keyboard.clear()
        for i in alco:
            keyboard1.row(i)
        bot.send_message(message.chat.id, 'Что ищете?', reply_markup=keyboard1)
    elif message.text.lower() in alco_low:
        keyboard1.keyboard.clear()
        keyboard1.row('найти новую позицию')
        bot.send_message(message.chat.id, a, reply_markup=keyboard1)
    elif message.text.lower() == 'найти новую позицию':
        keyboard1.keyboard.clear()
        for i in cities:
            keyboard1.row(i)
        bot.send_message(message.chat.id, 'Где вы находитесь?', reply_markup=keyboard1)
                #bot.send_contact(message.chat.id, phone_number='+79996664444', first_name='Нурсултан', last_name='Назарбаев')



@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)


bot.polling()
