from typing import Callable, Dict, Any, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, User
from loguru import logger


class LoggerMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:
        user: User = data.get("event_from_user")
        username = ''
        log_message = None
        if user.username is not None:
            username = f"(@{user.username})"

        if event.message is not None:
            log_message = (f'[Message] Text: "{event.message.text}". '
                           f'User: {user.full_name} | ID: {user.id} {username}')
        elif event.callback_query is not None:
            log_message = (f'[Callback] query: "{event.callback_query.data}". '
                           f'User: {user.full_name} | ID: {user.id} {username}')
        if log_message is not None:
            logger.info(log_message)
        result = await handler(event, data)
        return result
