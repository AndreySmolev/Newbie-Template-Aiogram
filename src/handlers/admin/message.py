import html

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from ...filters.check_admin import IsAdmin

router = Router()


async def admin_handler(message: Message):
    await message.answer(f'Welcome to admin menu, {html.escape(message.from_user.full_name)}')


def register_handlers():
    router.message.register(admin_handler, Command('admin'), IsAdmin())

