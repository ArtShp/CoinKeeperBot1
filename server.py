import os
import logging
import codecs

from aiogram import Bot, Dispatcher, executor, types
from jinja2 import Template


API_TOKEN = os.getenv('TELEGRAM_API_TOKEN')

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start', 'help'])
async def start_message(message: types.Message):
    with codecs.open('templates/start.html') as file:
        template = Template(file.read())
        await message.reply(template.render(username=message.chat.username),
                                            parse_mode='HTML', reply=False)
