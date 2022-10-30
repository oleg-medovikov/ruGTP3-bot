from aiogram import Bot, Dispatcher, types
import asyncio

from conf import BOT_API
from func import genarate_text

bot = Bot(token=BOT_API)
dp  = Dispatcher(bot)

@dp.message_handler(commands='start')
async def send_welcome(message: types.Message):
    try:
        await message.delete()
    except: pass

    return await message.answer('напишите что-нибудь')

@dp.message_handler( content_types=['text'] )
async def keys_for_generate(message: types.Message):
    await message.answer('минуточку')
    TEXT = message['text']

    genarated = genarate_text(TEXT)

    for text in genarated:
        await message.answer(text)


if __name__ == '__main__':
    try:
        while True:
            try:
                asyncio.run( dp.start_polling() )
            except:
                asyncio.sleep(5)
    except KeyboardInterrupt:
        pass
