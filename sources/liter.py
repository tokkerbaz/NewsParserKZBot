import json
import os
from aiogram import Bot, Dispatcher, executor, types
from config import token, user_id
from aiogram.utils.markdown import hbold, hunderline, hcode, hlink
from parsers import liter
from aiogram.dispatcher.filters import Text

bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


async def start(message):
    start_buttons = ["Все новости Liter", "Последние 5 новостей Liter", "Свежие новости Liter", "Меню"]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)

    await message.answer("Лента", reply_markup=keyboard)

async def get_all_news(message: types.Message):
    with open(f"{os.path.dirname(os.path.dirname(__file__))}/json/liter.json") as file:
        news_dict = json.load(file)

    for key, article in sorted(news_dict.items()):
        news = f"{hbold(article['article_date'])}\n{hlink(json.loads(article['article_title']),article['article_url'])}"

        await message.answer(news)

async def get_last_five(message: types.Message):
    with open(f"{os.path.dirname(os.path.dirname(__file__))}/json/liter.json") as file:
        news_dict = json.load(file)

    for key, article in sorted(news_dict.items())[-5:]:
        news = f"{hbold(article['article_date'])}\n{hlink(json.loads(article['article_title']),article['article_url'])}"

        await message.answer(news)


async def get_fresh_news(message: types.Message):
    fresh_news = liter.check_updates()

    if len(fresh_news) >= 1:
        for key, article in sorted(fresh_news.items())[-5:]:
            news = f"{hbold(article['article_date'])}\n{hlink(json.loads(article['article_title']),article['article_url'])}"
            await message.answer(news)
    else:
        await message.answer("Пока нет свежих новостей...")
