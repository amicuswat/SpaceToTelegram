import argparse
import os
from datetime import datetime

import requests
from dotenv import load_dotenv

from image_processing import download_image


def get_last_date_with_photos(params):
    response = requests.get("https://api.nasa.gov/EPIC/api/natural/all",
                            params=params)
    response.raise_for_status()

    return response.json()[0]["date"]


def fetch_nasa_epic_img(token, date=None):
    folder = os.path.join("images", "nasa_epic")

    params = {
        "api_key": token
    }

    if not date:
        date = get_last_date_with_photos(params)

    date = datetime.strptime(date, "%Y-%m-%d").date()

    year = date.strftime("%Y")
    month = date.strftime("%m")
    day = date.strftime("%d")

    response = requests.get(
        f"https://api.nasa.gov/EPIC/api/natural/date/{date}",
        params=params)
    response.raise_for_status()

    image_names = [obj['image'] for obj in response.json()]

    for img in image_names:
        image_url = f"https://api.nasa.gov/EPIC/archive/natural/" \
                    f"{year}/{month}/{day}/png/{img}.png"

        download_image(image_url, img_folder=folder, params=params)


if __name__ == "__main__":
    load_dotenv()
    token = os.environ['NASA_API_KEY']

    parser = argparse.ArgumentParser()
    parser.add_argument("--date", help="Enter desired date "
                                       "to fetch photos in format: YYYY-MM-DD",
                        default=None)
    args = parser.parse_args()

    fetch_nasa_epic_img(token, date=args.date)
