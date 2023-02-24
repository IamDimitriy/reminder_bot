
import time
import logging
from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove

# @dp.message_handler(commands=["start"])


async def start(message: types.Message):
    user_full_name = message.from_user.full_name
    #logging.info(f"{user_id=} {user_full_name=} {time.asctime()}")
    mess = f"Привет, {user_full_name}! Я буду напоминать тебе о всех твоих делах! Нужна помощь? Введи '/help'"
    await bot.send_message(message.from_user.id, mess, reply_markup=kb_client)


# @dp.message_handler(commands=["help"])
async def help(message: types.Message):
    mess = "Воспользуйся кнопками :)"
    await bot.send_message(message.from_user.id, mess)


@dp.message_handler(commands=["Новое напоминание"])
async def add(message: types.Message):
    while __name__ == "__main__":
        what = input("О чем напомнить?\nДля выхода тыкни '/exit'\n")
        if what == "/exit":
            break
        else:
            t = input("Через сколько минут напомнить?")
            t = int(t)*60
            time.sleep(t)
    await bot.send_message(message.from_user.id, what, reply_markup=ReplyKeyboardRemove())


def register_handler_client(dp: Dispatcher):
    dp.register_message_handler(start, commands=["start"])
    dp.register_message_handler(help, commands=["help"])
    dp.register_message_handler(add, commands=["Новое напоминание"])
