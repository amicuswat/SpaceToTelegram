import os
import random

from pathlib import Path
from urllib.parse import urlparse

import requests


def get_file_extention(url):
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)
    filename, extention = os.path.splitext(filename)
    return extention


def download_image(url, path=None, params=None):
    if not path:
        path = os.path.join("images", "misc")
    Path(path).mkdir(parents=True, exist_ok=True)

    hash = random.getrandbits(128)

    filename = "%032x" % hash
    extension = get_file_extention(url)
    filename = filename + extension
    filename = Path(path, filename)

    response = requests.get(url, params=params)
    response.raise_for_status()

    with open(filename, "wb") as file:
        file.write(response.content)
