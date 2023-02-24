
from handlers import admin, client
import time
import logging
from aiogram import executor
from create_bot import dp


async def on_startup(_):
    print("Bot is online")
client.register_handler_client(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)


"""
#с другой библиотекой
bot = telebot.TeleBot(TOKEN)
all_reminders = {}


@bot.message_handler(commands=["start"])
def start(message):
    mess = f"Привет, {message.from_user.first_name}! Я буду напоминать тебе о всех твоих делах! Только введи '/help'"
    bot.send_message(
        message.chat.id, mess)


def get_user_txt(message):
    if message.text == "Напоминания":
        mess = "Я напомню о:", all_reminders
        bot.send_message(
            message.chat.id, mess)


@bot.message_handler(commands=["help"])
def record(message):
    markup = types.ReplyKeyboardMarkup()
    rec = types.KeyboardButton("ЗАПИСЬ")

    markup.add(rec)
    bot.send_message(message.chat.id, "Что хочешь сделать?",
                    reply_markup=markup)


bot.polling(none_stop=True)
"""
