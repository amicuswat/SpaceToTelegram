import os
import random

from pathlib import Path
from urllib.parse import urlparse

import requests


def get_file_extension(url):
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)
    filename, extension = os.path.splitext(filename)
    return extension


def get_filename(url, img_folder):
    if not img_folder:
        img_folder = os.path.join("images", "misc")
    Path(img_folder).mkdir(parents=True, exist_ok=True)

    name_hash = random.getrandbits(128)

    filename = "%032x" % name_hash
    extension = get_file_extension(url)
    filename = f"{filename}{extension}"
    return Path(img_folder, filename)


def download_image(url, img_folder=None, params=None):
    filename = get_filename(url, img_folder)

    response = requests.get(url, params=params)
    response.raise_for_status()

    with open(filename, "wb") as file:
        file.write(response.content)
