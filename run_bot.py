import asyncio
import logging
from bot.main import run_bot

logging.basicConfig(level=logging.INFO, filename="bot_log.log", filemode="a",
                    format=" %(levelname)s: %(asctime)s -- %(name)s -- %(message)s")
log = logging.getLogger('bot')

if __name__ == '__main__':
    asyncio.run(run_bot())
