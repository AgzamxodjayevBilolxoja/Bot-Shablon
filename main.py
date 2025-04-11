from aiogram import executor

from loader import dp, bot, db
from config import ADMINS
from services.database.sql import create_table_user
import handlers

def main():
    
    db.execute(sql=create_table_user, commit=True)
    
    async def on_startup():
        try:
            for admin in ADMINS:
                await bot.send_message(admin, "✅ Bot ishga tushdi!")
        except Exception as e:
            print(f"Admin xabari yuborilmadi: {e}")

    executor.start_polling(dp, skip_updates=True, on_startup=on_startup())

if __name__ == "__main__":
    main()