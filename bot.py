import asyncio
import logging
from aiogram import Bot, Dispatcher
from config.config import Config, load_config
from handlers import user_handlers

# Инициализируем логгер
logger = logging.getLogger(__name__)


async def main() -> None:
    # Конфигурируем логирование
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')

    # Выводим в консоль информацию о начале запуска бота
    logger.info('Starting bot')

    config: Config = load_config('.env')
    bot: Bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    dp: Dispatcher = Dispatcher()
    dp.include_router(user_handlers.router)
    await bot.delete_webhook(drop_pending_updates=False)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
