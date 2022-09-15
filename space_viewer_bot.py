import os
from os import walk

import telegram
from dotenv import load_dotenv
from telegram import InputMediaPhoto, InputMediaDocument


def get_all_images(directory):
    images_tree = list(os.walk(directory))

    all_images = []
    while images_tree:
        elm = images_tree.pop()
        path, subdirs, filenames = elm
        if filenames and not subdirs:
            for name in filenames:
                all_images.append(os.path.join(path, name))

    return all_images



load_dotenv()
token = os.getenv('TG_TOKEN')
channel_id = os.getenv('TG_CHANNEL_ID')

bot = telegram.Bot(token=token)

# TODO - check file size
# TODO - select random file
# TODO - introduct time delay
# TODO - introduce async exit interface
# bot.send_message(chat_id=channel_id, text="Logem impsum test2")
# image = InputMediaDocument(media=open('images/apods/earthrise_lo1.gif', 'rb'))
# images = [image,]

# bot.send_media_group(chat_id=channel_id, media=images)

# filenames = next(walk("images"), (None, None, []))[2]
# filenames = next(walk("images"), (None, None, []))[2] # [] if no file
# print(filenames)



print(get_all_images("images"))
#
# for obj in images_in_dirs:
#     print(obj)
