from aiogram.types import ReplyKeyboardMarkup, KeyboardButton  # , ReplyKeyboardRemove

b1 = KeyboardButton("/Все напоминания")
b2 = KeyboardButton("/Новое напоминание")
b3 = KeyboardButton("/Удалить напоминание")

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(b2).row(b1, b3)
