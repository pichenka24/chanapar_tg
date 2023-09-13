import logging
from pyrogram import Client
from aiogram import Bot, Dispatcher

API_TOKEN = '6078129245:AAHQxuSo38lJuYb-VbU23VBNUXNRZ-Ge32s'
api_id = '18080688'
api_hash = '082e24aef968939f638f7af5813e583a'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
app = Client("coolprich", api_id, api_hash)