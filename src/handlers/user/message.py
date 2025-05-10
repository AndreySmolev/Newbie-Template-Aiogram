import html

from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

import src.services as repo
import src.keyboards.user as kb

router = Router()


async def start_handler(message: Message):
    await repo.create_user(user_id=message.from_user.id)
    await message.answer(f'Hi, {html.escape(message.from_user.full_name)}',
                         reply_markup=kb.start_menu)


async def menu_handler(message: Message):
    await message.answer('Menu', reply_markup=kb.sub_menu)


def register_handlers():
    router.message.register(start_handler, CommandStart())
    router.message.register(menu_handler, Command('menu'))
    router.message.register(menu_handler, F.text == 'menu')
