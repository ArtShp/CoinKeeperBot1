import os
import logging
import codecs
import expences
import exception

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


@dp.message_handler()
async def add_expence(message: types.Message):
    try:
        expence = expences.add_expence(message.text)
    except exception.NotCorrectMessage as e:
        await message.reply(str(e), reply=False)
        return
    answer_message = (
        f'Добавлены траты {expence.amount} рублей на {expence.category_name}\n\n'
        f'Здесь выведем статистику за сегодня'
    )
    await message.reply(answer_message, reply=False)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
