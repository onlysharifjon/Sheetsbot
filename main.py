import logging

import openpyxl
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

TOKEN = '6988980301:AAHtfRkFbZo1R-HexBLovgrm0OX3Bl-Dalo'

bot = Bot(token=TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, storage=MemoryStorage())
logging.basicConfig(level=logging.INFO)

# Middleware for logging
dp.middleware.setup(LoggingMiddleware())

import os


@dp.message_handler(commands='start')
async def start_command(message: types.Message):
    await message.reply('Assalomu Aleykum {}!'.format(message.from_user.first_name))
    await message.answer('.XLSX yoki .xlsx formatdagi file jo`nating !')


from excel import read_excel_part1

#
@dp.message_handler(content_types=types.ContentTypes.DOCUMENT)
async def file_handler(message: types.Message):
    file_name = message.document.file_name
    if file_name.lower().endswith('.xlsx'):
        await message.document.download(f'uploads/{file_name}')
        await message.answer('Fayl yuklandi!')
        # os.remove(f'uploads/{file_name}')
        txt = read_excel_part1(path=f'uploads/{file_name}', file_name=file_name)
        await message.answer(txt)

    else:
        await message.answer('.XLSX yoki .xlsx formatdagi faylni yuboring!')


if __name__ == '__main__':
    from aiogram import executor

    executor.start_polling(dp, skip_updates=True)
