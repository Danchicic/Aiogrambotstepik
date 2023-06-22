from aiogram.filters import Command, CommandStart, Text
from aiogram import Router
from aiogram.types import Message, CallbackQuery

from filters.game_filter import game_filter
from lexicon.lexicon_ru import LEXICON_RU
import Keyboards as keyb

router: Router = Router()
router.message.filter(game_filter)


@router.message(CommandStart())
async def start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'], reply_markup=keyb.User_kb.kb)


@router.message(Command(commands='help'))
async def help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'])


@router.callback_query(Text(text='ушел в избранное'))
async def callself(callback: CallbackQuery):
    await callback.answer()
