import os
import logging
import codecs
import expenses
import exception

from categories import Categories
from middleware import AccessMiddleware

from aiogram import Bot, Dispatcher, executor, types
from jinja2 import Template

logging.basicConfig(level=logging.INFO)

API_TOKEN = os.getenv('TELEGRAM_API_TOKEN')
ACCESS_ID = os.getenv('TELEGRAM_ACCESS_ID')

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot=bot)
dp.middleware.setup(AccessMiddleware(ACCESS_ID))


@dp.message_handler(commands=['start', 'help'])
async def start_message(message: types.Message):
    with codecs.open('templates/start.html') as file:
        template = Template(file.read())
        await message.reply(template.render(username=message.chat.username),
                                            parse_mode='HTML')


@dp.message_handler()
async def add_expence(message: types.Message):
    try:
        expence = expenses.add_expence(message.text)
    except exception.NotCorrectMessage as e:
        await message.reply(str(e))
        return
    answer_message = (
        f'Добавлены траты {expence.amount} рублей на {expence.category_name}\n\n'
        f'Здесь выведем статистику за сегодня'
    )
    await message.reply(answer_message)

@dp.message_handler(lambda message: message.text.startswith('/del'))
async def del_expence(message: types.Message):
    """Удаление расхода"""
    row_id = int(message.text[4:])
    expenses.delete_expense(row_id)
    answer_message = 'Удалил!'
    await message.answer(answer_message)

@dp.message_handler(commands=['today'])
async def today_stats(message: types.Message):
    """Дневная статистика по расходам"""
    answer_message = expenses.get_today_statistics()
    await message.answer(answer_message)

@dp.message_handler(commands=['month'])
async def month_stats(message: types.Message):
    """Месячная статистика по расходам"""
    answer_message = expenses.get_month_statistics()
    await message.answer(answer_message)

@dp.message_handler(commands=['categories'])
async def categories_list(message: types.Message):
    """Категории по расходам"""
    categories = Categories().get_all_categories()
    with codecs.open('templates/categories.html') as file:
        template = Template(file.read())
        await message.reply(template.render(categories=categories),
                            parse_mode='HTML')

@dp.message_handler(commands=['expenses'])
async def expenses_list(message: types.Message):
    """Список последних расходов"""
    last_expenses = expenses.last()
    if not last_expenses:
        await message.answer('Расходов ещё не было записано!')
        return
    last_expenses_rows = [
        f'{expense.amount} рублей на {expense.category_name} - нажми /del{expense.id} для удаления расхода.'
        for expense in last_expenses
    ]
    answer_message = 'Последние траты: '.join(last_expenses_rows)
    await message.answer(answer_message)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
