from loader import dp
from aiogram.types import Message
import game





@dp.message_handler(commands=['set'])
async def mes_set(message: Message):
    count= message.text.split()[1]
    game.max_total= int(count)
    await message.answer(f'Установили новое кол-во конфет в размере - {game.max_total}')