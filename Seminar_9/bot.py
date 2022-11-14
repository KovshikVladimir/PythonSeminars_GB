from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.utils.markdown import text
from aiogram.dispatcher import Dispatcher
import youtube_download_cli as dwnld
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет! Введи ссылку нужного видео: ") 
                        # txt = msg.from_user.id)
                        # dwnld.download(txt)

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply('Введи ссылку на нужное видео ')


if __name__ == '__main__':
    executor.start_polling(dp)