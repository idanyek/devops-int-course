import asyncio, logging
from aiogram import Bot, Dispatcher, types

BOT_TOKEN = "6792265112:AAGEc3rii_TrsGO7zoieiaKMUMfZP-hiL9E"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message()
async def answer_as_echo(message: types.Message):
    await message.answer(text=message.text)


async def main():
    logging.basicConfig(level=logging.DEBUG)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
