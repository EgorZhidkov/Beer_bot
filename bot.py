import telebot
import random
from telebot.types import Message
from classbeer import Beer

TOKEN = '927282765:AAHUsLXygHVabpQvNyl1IS-XD219jNDTSKw'
bot = telebot.TeleBot(TOKEN)
first_beer = Beer(54.80, "Velkopopovicky Kozel", 3.7, "Темное", 0.45)
second_beer = Beer(54.90, "Velkopopovicky Kozel", 4, "Светлое", 0.45)
third_beer = Beer(39.90, "Хамовники", 4.5, "Светлое", 0.47)
a = "cjbgif"
myArray = [first_beer, second_beer, third_beer]
index = 0
def search(message):
    for b in range(myArray.__len__()):
        if message.text == myArray[b].get_value():
            test = b
            repr(myArray[test])


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Здравствуйте,я бот по подбору пива, дальше от вас требуется ввести параметры,по одному в "
                          "каждое сообщение: цена, название, крепость, вид, размер ")


@bot.message_handler(content_types=['text'])
def check_id_sticker(message):
    for i in range(myArray.__len__()):
        if message.text == myArray[i].get_value():
            test = i
            repr(myArray[test])
    bot.send_message(message.chat.id, repr(myArray[test]))


bot.polling(timeout=60)
