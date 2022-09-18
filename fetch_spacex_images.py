import argparse
import os

import requests

from image_processing import download_image


def get_last_launch_id():
    response = requests.get("https://api.spacexdata.com/v5/launches")
    response.raise_for_status()

    launches_with_images = [obj for obj in response.json()
                            if obj['links']['flickr']['original']]

    return launches_with_images.pop()['id']


def fetch_spacex_launch_imgs(launch_id=None):
    folder = os.path.join("images", "spaceX")

    if not launch_id:
        launch_id = get_last_launch_id()

    response = requests.get(
        f"https://api.spacexdata.com/v5/launches/{launch_id}")
    response.raise_for_status()

    urls = response.json()['links']['flickr']['original']

    for url in urls:
        download_image(url, path=folder)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--launch_id', help="launch id photos of which you "
                        "want fetch")
    args = parser.parse_args()

    fetch_spacex_launch_imgs(launch_id=args.launch_id)
