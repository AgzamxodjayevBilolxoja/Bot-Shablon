from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from services.database.database import Database
from config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN, parse_mode="HTML")

storage = MemoryStorage()

dp = Dispatcher(storage=storage)

db = Database()