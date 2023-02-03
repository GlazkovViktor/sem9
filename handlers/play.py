from loader import dp
from aiogram.types import Message
import game


    


@dp.message_handler(commands=['play'])
async def mes_start(message: Message):
    for duel in game.total:
        if message.from_user.id == duel[0]:
            await message.answer(f'{duel[1]}, братишка, ты уже начал игру')
            break 
    else:
        await message.answer(f'{message.from_user.full_name}, игра началась!\n'   
                         f'Бери от 1 до 28 конфеты ')
        my_game=[message.from_user.id, message.from_user.first_name, game.max_total]
        game.total.append(my_game)

 