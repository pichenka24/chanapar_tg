from datetime import date
from data import dict
import time
import asyncio

from config import bot


async def birthday():
    today = date.today()
    current_date = str(today).replace('-', '.')[5:]
    for name in dict:
        if current_date == dict[name]:
            await bot.send_message(chat_id=-1001616867686,
                                   text=f'Сегодня в Чанапаре празднуется День Рождения -> {name}')


while True:
    asyncio.run(birthday())
    time.sleep(86400)




