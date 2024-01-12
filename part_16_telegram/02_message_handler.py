import asyncio, logging, os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types

# loading .env file
load_dotenv()

#getting token from env file
bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher()

@dp.message()
async def answer_as_echo(message: types.Message):
    await message.answer(text=message.text)


async def main():
    logging.basicConfig(level=logging.DEBUG)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
