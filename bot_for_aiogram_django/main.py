from aiogram.utils import executor

from bot_app.bot import dp

if __name__ == '__main__':
    """
    If you wanna start the bot - run this file "main.py" 
    Don't remember start the django project
    """
    executor.start_polling(dispatcher=dp, skip_updates=True, timeout=999999)
