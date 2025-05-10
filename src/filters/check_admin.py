from aiogram.filters import BaseFilter
from aiogram.types import TelegramObject

from ..core.config import Settings


class IsAdmin(BaseFilter):

    def __init__(self):
        config = Settings()
        self.admin_ids = config.ADMIN_IDS

    async def __call__(self, obj: TelegramObject) -> bool:
        return obj.from_user.id in self.admin_ids
