import asyncio
import sys

from loguru import logger
from os import environ

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from filters.chat_type import ChatTypeFilter
from middlewares.logger import LoggerMiddleware
from core.router_manager import setup_routers

from core.config import Settings
from src.core.db import db


async def main():
    logger.add(sys.stderr, format="{time} {level} {message}", filter="template", level="INFO")

    environ['TZ'] = 'Europe/Moscow'
    logger.error("Starting bot")
    config = Settings()
    router = setup_routers()

    bot = Bot(token=config.BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    bot_info = await bot.get_me()

    await db.connect()

    dp = Dispatcher(config=config, bot_info=bot_info, db=db)
    dp.include_routers(router)

    dp.update.outer_middleware(LoggerMiddleware())

    dp.message.filter(
        ChatTypeFilter(chat_type=["private"])
    )

    try:
        logger.error(f'Bot {bot_info.full_name} started (@{bot_info.username}. ID: {bot_info.id})')
        await dp.start_polling(bot)
    finally:
        await bot.session.close()
        await db.close()


def cli():
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")


if __name__ == '__main__':
    cli()
