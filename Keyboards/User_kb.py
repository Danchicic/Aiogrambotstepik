from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardButton
from aiogram.types import KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

buttons = [KeyboardButton(text='Камень'), KeyboardButton(text='Ножницы'), KeyboardButton(text='Бумага')]
ibuttons = [InlineKeyboardButton(text='Перейти в избранное', callback_data='ушел в избранное')]
kb: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=[ibuttons])

