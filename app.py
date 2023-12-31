from aiogram import executor

from loader import dp
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
import middlewares,  handlers

async def on_startup(dp):
    # Birlamchi komandalar (/star va /help)
    await set_default_commands(dp)

    # Bot ishga tushgani haqida adminga xabar berish
    await on_startup_notify(dp)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
