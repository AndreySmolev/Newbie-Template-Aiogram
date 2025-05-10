from aiogram import Router, F
from aiogram.types import CallbackQuery

from ...filters.check_admin import IsAdmin

router = Router()


async def admin_cancel_handler(query: CallbackQuery):
    await query.message.edit_text('Operation canceled')


def register_handlers():
    router.callback_query.register(admin_cancel_handler, F.data == 'cancel', IsAdmin())
