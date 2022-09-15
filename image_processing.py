import os
from pathlib import Path
from urllib.parse import urlparse

import requests


def get_file_extention(url):
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)
    filename, extention = os.path.splitext(filename)
    return extention


def download_image(url, path="images/misc"):
    Path(path).mkdir(parents=True, exist_ok=True)

    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)
    filename = Path(path, filename)

    response = requests.get(url)
    response.raise_for_status()

    with open(filename, "wb") as file:
        file.write(response.content)
