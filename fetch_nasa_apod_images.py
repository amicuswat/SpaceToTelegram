import argparse
import os

import requests
from dotenv import load_dotenv

from image_processing import download_image


def fetch_apod(token, count=5):
    params = {
        "api_key": token,
        "count": count
    }
    folder = os.path.join("images", "apods")

    response = requests.get('https://api.nasa.gov/planetary/apod',
                            params=params)
    response.raise_for_status()

    for obj in response.json():
        if obj['media_type'] == 'image':
            download_image(obj['url'], path=folder)


if __name__ == "__main__":
    load_dotenv()
    token = os.environ['NASA_API_KEY']

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--count", help="How many pictures of the day to download", default=5)
    args = parser.parse_args()

    fetch_apod(token, count=args.count)
