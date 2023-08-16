from aiogram import Bot, Dispatcher

from bot.config.settings import settings
from bot.endpoints.handlers import router

TG_TOKEN = settings.TOKEN

bot = Bot(token=TG_TOKEN)
dp = Dispatcher()

dp.include_router(router)


async def run_bot():
    await dp.start_polling(bot)
