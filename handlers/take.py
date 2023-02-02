from loader import dp
from aiogram.types import Message
import game
import random


@dp.message_handler()
async def mes_start(message: Message):
        for duel in game.total:
            if message.from_user.id == duel[0]:
                count = message.text
                name = message.from_user.first_name
                if count.isalpha():
                    await message.answer(f'{name}, братишка, возьми допустимое ЧИСЛО конфет от 1 до 28, что ты тут мне пишешь')
                elif count.isdigit() and 0 < int(count) <= 28:
                    duel[2] -= int(count)
                    if await check_win(message, 'Ты',duel):
                        return True
                    await message.answer(f'{duel[1]} взял {count} конфет и на столе осталось {duel[2]}\n'
                                        f'Теперь ход бота')
                    bot_take = random.randint(1, 28) if duel[2] > 28 else duel[2]
                    duel[2] -= bot_take
                    if await check_win(message, 'Бот', duel):
                        return True 
                    await message.answer(f'Бот Валера взял {bot_take} конфет и на столе осталось {duel[2]}\n'
                                            f'Теперь твой ход')
                else:
                    await message.answer(f'{name}, братишка, возьми допустимое количество конфет')


async def check_win(message: Message, win: str, total: list):
    if total[2] <= 0:
        await message.answer(f'{win} ПОБЕДИЛ! Поздравляю!')
        game.total.remove(total)
        return True
    return False
