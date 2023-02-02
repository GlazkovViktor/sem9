from loader import dp
from aiogram.types import Message
import game



@dp.message_handler(commands=['start'])
async def mes_start(message: Message):
    for duel in game.total:
        if message.from_user.id == duel[0]:
            await message.answer(f'{duel[1]}, братишка, ты уже начал игру')
            break 
    else:
        # game.new_game = True
        await message.answer(f'Привет,  {message.from_user.full_name},\n'   
                         f'Мы будем играть в конфеты, бери от 1 до 28') 
        my_game=[message.from_user.id, message.from_user.first_name, 150]
        game.total.append(my_game)

 