from aiogram.types import Message
from aiogram import F


def game_filter(message: Message) -> bool:
    return F.text in ['Камень', 'Ножницы', 'Бумага']
