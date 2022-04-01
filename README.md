# NewsParserKZBot
Parsing news from (_Tengrinews, Newtimes, Liter, Informburo_) and sending them as message in Telegram

## Installation

Script requires following libs to be installed:

```sh
asyncio
aiogram
requests
bs4 (BeautifulSoup)
```

Install the dependencies.

```sh
cd NewsParserKZBot
pip3 install -r requirements.txt
```

## Usage

To run the script you need to:
- Create Telegram Bot (more info [core.telegram.org](https://core.telegram.org/bots#3-how-do-i-create-a-bot))
- Get `token` of your new created bot and paste it to `config.py` file (requires to be string)
- Get your `user_id/chat_id` (you can text to `@chatIDrobot` `/start` and get your `chat_id`) and paste it to `config.py` file
- Run `python tg_bot.py` in your terminal

## What bot do?

To run the bot you need to text `/start` then it will ask you to choose resource. There are 4 resource right now (_Tengrinews, Newtimes, Liter and Informburo_).
By picking needed resource, bot parses the latest (~20) news from resource's website and saves it to `json\{name_of_resource}.json` file.
After you picked resource, it asks to choose the option (All news, Last 5 news and Latest(Fresh)). So by choosing needed option it will send news as messages.

Also the boot is running in asyncio loop, so every 15 minutes, it checking for updates in all resources, if there is any updates, the bot will automatically send those as messages.
If there are any, then it will let you know, that there are any updates during this 15 minutes in `resource_name`.

The script will only work to its owner (attached by `user_id`), to avoid the bot to be used for all who texts.

## About project

This project is not to show skills, but was made in a road to learn python. So there are definetely more cons than pros. Thus, want to you, not judge me for mistakes. And there been only 2 monthes for me start to learn Python

## License

MIT

**Free Script, Hell Yeah!**
