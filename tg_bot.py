import asyncio
import json
from warnings import filters
from aiogram import Bot, Dispatcher, executor, types
from config import token, user_id
from aiogram.utils.markdown import hbold, hunderline, hcode, hlink
from aiogram.dispatcher.filters import Text, IDFilter
from sources import tengrinews as tn
from sources import newtimes as nt
from sources import liter as lt
from sources import informburo as ib
from parsers import tengrinews,newtimes,informburo,liter


bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

# На Главную
@dp.message_handler(Text(equals="Меню"), chat_id=user_id)
@dp.message_handler(commands="start", chat_id=user_id)
async def start(message: types.Message):
    start_buttons = ['Tengrinews','Newtimes','Informburo', 'Liter']
    #start_buttons = ["Все новости", "Последние 5 новостей", "Свежие новости"]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)

    await message.answer("Выберите Ресурс", reply_markup=keyboard)

# Tengrinews commands for Bot
@dp.message_handler(Text(equals="Tengrinews"), chat_id=user_id)
async def startTn(message):
    await tn.start(message)

@dp.message_handler(Text(equals="Все новости Tengrinews"), chat_id=user_id)
async def get_all_newsTn(message: types.Message):
    await tn.get_all_news(message)

@dp.message_handler(Text(equals="Последние 5 новостей Tengrinews"), chat_id=user_id)
async def get_last_fiveTn(message: types.Message):
    await tn.get_last_five(message)

@dp.message_handler(Text(equals="Свежие новости Tengrinews"), chat_id=user_id)
async def get_fresh_newsTn(message: types.Message):
    await tn.get_fresh_news(message)



# Newtimes commands for Bot
@dp.message_handler(Text(equals="Newtimes"), chat_id=user_id)
async def startNt(message):
    await nt.start(message)

@dp.message_handler(Text(equals="Все новости Newtimes"), chat_id=user_id)
async def get_all_newsNt(message: types.Message):
    await nt.get_all_news(message)

@dp.message_handler(Text(equals="Последние 5 новостей Newtimes"), chat_id=user_id)
async def get_last_fiveNt(message: types.Message):
    await nt.get_last_five(message)

@dp.message_handler(Text(equals="Свежие новости Newtimes"), chat_id=user_id)
async def get_fresh_newsNt(message: types.Message):
        await nt.get_fresh_news(message)



# Informburo commands for Bot
@dp.message_handler(Text(equals="Informburo"), chat_id=user_id)
async def startIb(message):
    await ib.start(message)

@dp.message_handler(Text(equals="Все новости Informburo"), chat_id=user_id)
async def get_all_newsIb(message: types.Message):
    await ib.get_all_news(message)

@dp.message_handler(Text(equals="Последние 5 новостей Informburo"), chat_id=user_id)
async def get_last_fiveIb(message: types.Message):
    await ib.get_last_five(message)

@dp.message_handler(Text(equals="Свежие новости Informburo"), chat_id=user_id)
async def get_fresh_newsIb(message: types.Message):
        await ib.get_fresh_news(message)
        


# Liter commands for Bot
@dp.message_handler(Text(equals="Liter"), chat_id=user_id)
async def startLt(message):
    await lt.start(message)

@dp.message_handler(Text(equals="Все новости Liter"), chat_id=user_id)
async def get_all_newsLt(message: types.Message):
    await lt.get_all_news(message)

@dp.message_handler(Text(equals="Последние 5 новостей Liter"), chat_id=user_id)
async def get_last_fiveLt(message: types.Message):
    await lt.get_last_five(message)

@dp.message_handler(Text(equals="Свежие новости Liter"), chat_id=user_id)
async def get_fresh_newsLt(message: types.Message):
        await lt.get_fresh_news(message)

async def news_every_min(source):
    while True:
        if source == 'tengrinews':
            fresh_news = tengrinews.check_updates()
        elif source == 'newtimes':
            fresh_news = newtimes.check_updates()
        elif source == 'informburo':
            fresh_news = informburo.check_updates()
        elif source == 'liter':
            fresh_news = liter.check_updates()
        else:
            fresh_news = tengrinews.check_updates()

        if len(fresh_news) >= 1:
            for key, article in sorted(fresh_news.items())[-5:]:
                news = f"{hbold(article['article_date'])}\n{hlink(json.loads(article['article_title']),article['article_url'])}"
                await bot.send_message(user_id, news)

        else:
            await bot.send_message(user_id, f"Пока нет свежих новостей у {hbold(source)}...", disable_notification=True)

        await asyncio.sleep(900)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(news_every_min('infromburo'))
    loop.create_task(news_every_min('liter'))
    loop.create_task(news_every_min('newtimes'))
    loop.create_task(news_every_min('tengrinews'))
    executor.start_polling(dp)