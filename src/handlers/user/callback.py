from aiogram import Router, F
from aiogram.types import CallbackQuery

router = Router()


async def cancel_handler(query: CallbackQuery):
    await query.message.edit_text('Operation canceled')


def register_handlers():
    router.callback_query.register(cancel_handler, F.data == 'cancel')
