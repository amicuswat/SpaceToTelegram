import argparse

from image_processing import download_image

import requests


def get_last_launch_id():
    response = requests.get("https://api.spacexdata.com/v5/launches")
    response.raise_for_status()

    launches_with_images = []
    for obj in response.json():
        if obj['links']['flickr']['original']:
            launches_with_images.append(obj)

    return launches_with_images.pop()['id']


def fetch_spacex_launch_imgs(launch_id=None):

    if not launch_id:
        launch_id = get_last_launch_id()

    response = requests.get(
        f"https://api.spacexdata.com/v5/launches/{launch_id}")

    urls = response.json()['links']['flickr']['original']

    for url in urls:
        download_image(url, "images/spaceX")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--launch_id', help="launch id photos of which you "
                                          "want fetch")
    args = parser.parse_args()

    fetch_spacex_launch_imgs(launch_id=args.launch_id)
