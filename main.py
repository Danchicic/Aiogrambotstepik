from aiogram import Bot, types, Dispatcher, executor
from aiogram.types import ReplyKeyboardMarkup
from random import randint
import datetime
import asyncio
import aioschedule

hour = "%d" % datetime.datetime.now().hour

bot = Bot(token='')
dp = Dispatcher(bot)
default_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
default_kb.add('Да')
default_kb.add('Нет')
kb_n = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_n.add('Заняться своим здоровьем')
kb_thx = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_thx.add('Спасибо')


def unparse():
    rows = []
    with open('soviets') as f:
        for row in f:
            rows.append(row[:-1])
    return rows[randint(0, len(rows) - 1)]


@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    global chat_id
    chat_id = message['chat']['id']
    await message.answer(
        'Привет\nЯ бот который помогает бросить вредные привычки\nОдна сигарета отнимает 15 минут жизни, и ты до сих пор куришь?')
    await message.answer('Напиши сколько сигарет ты выкуриваешь в день')


@dp.message_handler(text=['Да', 'Заняться своим здоровьем'])
async def if_y(msg: types.Message):
    await msg.answer(
        'Ты сделал правильный выбор, и я тебе помогу в этом\nЯ буду присылать тебе совет каждый день\nЧтоб тебе было легче бросить курить',
        reply_markup=kb_thx)


@dp.message_handler(text='Нет')
async def if_n(msg: types.Message):
    await msg.answer(f'Надеюсь ты передумаешь и займешься своим здоровьем', reply_markup=kb_n)


@dp.message_handler()
async def answer_smoke(msg: types.Message):
    if msg['text'].isdigit():
        c = 15 * int(msg['text'])
        await msg.answer(f'Ты теряешь {c} минут жизни в день\nТы хочешь Бросить курить?', reply_markup=default_kb)
    else:
        await bot.send_message(chat_id=msg['chat']['id'], text=unparse())


async def send_sov():
    await bot.send_message(chat_id=chat_id, text=unparse())


async def scheduler():
    aioschedule.every().day.at("10:00").do(send_sov)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


async def on_startup(dp):
    asyncio.create_task(scheduler())


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp, skip_updates=True, on_startup=on_startup)
