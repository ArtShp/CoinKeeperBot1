"""Аутентификация - пускаем только конкретного пользователя"""
from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware

class AccessMiddleware(BaseMiddleware):
    def __init__(self, user_id: int):
        self.access_id = user_id
        super().__init__()

    async def when_message(self, message:types.Message, _):
        if int(message.from_user.id) != int(self.access_id):
            await message.answer('Доступ запрещён!')
            raise CancelHandler()
