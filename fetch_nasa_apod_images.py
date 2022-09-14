import os
import argparse
from dotenv import load_dotenv

from image_processing import download_image

import requests

def fetch_apod(token, count=5):
    params = {
        "api_key": token,
        "count": count
    }

    response = requests.get('https://api.nasa.gov/planetary/apod',
                            params=params)
    for obj in response.json():
        download_image(obj['url'], path="images/apods")


if __name__ == "__main__":
    load_dotenv()
    token = os.getenv('NASA_API_KEY')

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--count", help="How many pictures of the day to download")
    args = parser.parse_args()

    if args.count:
        fetch_apod(token, count=args.count)
    else:
        fetch_apod(token)