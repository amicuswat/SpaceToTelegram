import argparse
import os
import random
import time

import telegram
from dotenv import load_dotenv
from PIL import Image
from telegram import InputMediaDocument


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


def make_image_smaller(image_path, max_size):

    ratio = max_size/os.path.getsize(image_path)

    image = Image.open(image_path)

    new_width = int(image.width * ratio)
    new_height = int(image.height * ratio)

    image.thumbnail((new_width, new_height))
    image.save(image_path)

    return image_path


if __name__ == "__main__":
    load_dotenv()
    token = os.environ['TG_TOKEN']
    channel_id = os.environ['TG_CHANNEL_ID']

    MAX_IMG_SIZE = 20971520

    parser = argparse.ArgumentParser()
    parser.add_argument("--interval",
                        help="Set interval to send photos in hours",
                        type=int, default=4)
    args = parser.parse_args()

    bot = telegram.Bot(token=token)

    all_images = get_all_images("images")

    while True:
        if all_images:
            random.shuffle(all_images)
        else:
            all_images = get_all_images("images")

        image_path = all_images.pop()

        if os.path.getsize(image_path) >= MAX_IMG_SIZE:
            image_path = make_image_smaller(image_path, MAX_IMG_SIZE)

        image = InputMediaDocument(
            media=open(image_path, 'rb'))

        bot.send_media_group(chat_id=channel_id, media=[image])

        time.sleep(args.interval * 3600)
