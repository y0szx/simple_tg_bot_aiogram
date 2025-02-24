from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from decouple import config
import json
from pathlib import Path


ADMIN_ID = config("ADMIN_ID")
BOT_TOKEN = config("BOT_TOKEN")
HOST = config("HOST")
PORT = int(config("PORT"))
WEBHOOK_PATH = f'/{BOT_TOKEN}'
BASE_URL = config("BASE_URL")
DUTY_LIST_FILE = Path("duty_admins.json")


bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(
    parse_mode=ParseMode.HTML))
dp = Dispatcher()
duty_admins = set()


def load_duty_admins():
    if DUTY_LIST_FILE.exists():
        with open(DUTY_LIST_FILE, "r") as f:
            return set(json.load(f))
    return set()


def save_duty_admins(admins):
    with open(DUTY_LIST_FILE, "w") as f:
        json.dump(list(admins), f)


duty_admins = load_duty_admins()
