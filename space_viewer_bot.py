import os

import telegram
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('TG_TOKEN')
channel_id = os.getenv('TG_CHANNEL_ID')

bot = telegram.Bot(token=token)
bot.send_message(chat_id=channel_id, text="Logem impsum test2")
