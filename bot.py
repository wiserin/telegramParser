from aiogram import Bot
from dotenv import load_dotenv
import os

load_dotenv()

bot = Bot(os.getenv('TOKEN_FOR_TESTS'))