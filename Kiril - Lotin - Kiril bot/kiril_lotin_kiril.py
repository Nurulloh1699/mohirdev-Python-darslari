# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 10:45:31 2025

@author: DavrServis
"""

from transliterate import to_cyrillic, to_latin
import telebot

# print(to_latin('дастур'))
# print(to_cyrillic('dastur'))

# Keling endi shart beramiz va kiritilgan matnga qarab uni qarshi matnga (lotin bo'lsa, kirilga yoki aksincha) o'zgartiramiz.
TOKEN = '7831713346:AAGTz3g7UtWkyXmEB33DDNlXlGZSSANSGYw'
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    javob = "Assalomu Alekum, Xush kelibsiz!"
    javob += "\nMatn kiriting:"
    bot.reply_to(message, javob)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg = message.text
    
    javob = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    
    # if msg.isascii():
    #     javob = to_cyrillic(msg)
    # else:
    #     javob = to_latin(msg)
        
    bot.reply_to(message, javob(msg))



bot.infinity_polling()

# matn = input("Matn kiriting: ")

# if matn.isascii():
#     print(to_cyrillic(matn))
# else:
#     print(to_latin(matn))
