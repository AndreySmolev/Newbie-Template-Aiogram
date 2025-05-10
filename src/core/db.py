import aiosqlite

from ..core.config import Settings


class DBConnect:
    def __init__(self, db_url: str):
        self.db_url = db_url
        self.connection: aiosqlite.Connection = None
        self.cursor: aiosqlite.Cursor = None

    async def connect(self):
        self.connection = await aiosqlite.connect(self.db_url)
        self.cursor = await self.connection.cursor()

    async def close(self):
        await self.cursor.close()
        await self.connection.close()

    async def execute(self, query: str, params: tuple = ()):
        await self.cursor.execute(query, params)
        await self.connection.commit()

    async def fetchall(self, query: str, params: tuple = ()) -> list[tuple]:
        await self.cursor.execute(query, params)
        return await self.cursor.fetchall()

    async def fetchone(self, query: str, params: tuple = ()) -> tuple:
        await self.cursor.execute(query, params)
        return await self.cursor.fetchone()


settings = Settings()
db = DBConnect(settings.get_db_url())
