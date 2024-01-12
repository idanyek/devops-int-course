import asyncio, logging, os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types

# loading .env file
load_dotenv()

#getting token from env file
bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher()

@dp.message()
async def replay_as_echo(message: types.Message):
    try:
        await message.send_copy(chat_id=message.chat.id) #432654152
    except TypeError:
        await message.reply(text="sorry i get an error, please try again.")

    # if message.text:
    #     await message.reply(text=message.text)
    # elif message.sticker:
    #     await message.reply(text="thank you for the sticker!")
    #     await message.reply_sticker(sticker=message.sticker.file_id)
    # elif message.photo:
    #     await message.reply(text="i cant recived photos yet")
    # else:
    #     await message.reply(text="A new media type was used.")


@dp.message()
async def answer_as_echo(message: types.Message):
    await message.answer(text=message.text)


async def main():
    logging.basicConfig(level=logging.DEBUG)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
