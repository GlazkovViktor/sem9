from loader import dp
from aiogram.types import Message

    
@dp.message_handler(commands=['start'])
async def mes_help(message: Message):
     await message.answer(f'Привет,  {message.from_user.full_name},\n'   
                         f'Мы будем играть в конфеты, для того чтобы задать количество конфет напиши команту "/set" '
                         f' пробел "количетсво конфет" по умолчанию конфет 150, для начада игры введи команду "/play" ')
    