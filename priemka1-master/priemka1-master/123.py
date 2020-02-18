import telebot

telebot.apihelper.proxy = {'https':'https://176.241.138.70:50003'}

bot = telebot.TeleBot('854025714:AAH9Wi3_rWfVJvjnbDgNWkL8hYCbH2Fr-wY')
keyboard1 = telebot.types.ReplyKeyboardMarkup()

alco = ['Виски "Jameson"', 'Зеленая марка','777','blazer']
for i in alco:
    keyboard1.row(i)
bot.send_message(chat_id = 215482021, text = 'ты пидор')
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Давай найдем алкоголь! Что тебе нужно?', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    print(message)
    if message.text.lower() == 'виски \"jameson\"':
        bot.send_message(message.chat.id, 'в Ашане')
    elif message.text.lower() == 'зеленая марка':
        bot.send_message(message.chat.id, 'У казахов на втором этаже')
    elif message.text.lower() == 'я тебя люблю':
        bot.send_sticker(message.chat.id, 'CAADAgADZgkAAnlc4gmfCor5YbYYRAI')

@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)

bot.polling()