import os
from urllib.parse import urlparse
# import json

import requests
from pathlib import Path
from dotenv import load_dotenv

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





def fetch_nasa_epic_img(token):
    params = {
        "api_key": token
    }

    response = requests.get("https://api.nasa.gov/EPIC/api/natural/all", params=params)
    
    dates = []
    for obj in response.json():
        dates.append(obj["date"])

    response = requests.get(f"https://api.nasa.gov/EPIC/api/natural/date/{dates[0]}", params=params)
    
    images = []
    for obj in response.json():
        images.append(obj['image'])

    year, month, date = dates[0].split("-")

    for img in images:
        image_url = f"https://api.nasa.gov/EPIC/archive/natural/{year}/{month}/{date}/png/{img}.png?api_key={token}"
        print(image_url)
    
        download_image(image_url, "images/nasa_epic")


if __name__ == "__main__":
    load_dotenv()
    token = os.getenv('NASA_API_KEY')

    fetch_nasa_epic_img(token)


# print(json.dumps(response.json(), indent=2))
# print(response.json())

# with open('flights.txt', 'w') as file:
#     file.write(json.dumps(response.json(), indent=2))

# urls = ["https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg",
#        "https://kipmu.ru/wp-content/uploads/2021/03/hbbl.jpg",
#         "https://itzine.ru/wp-content/uploads/2019/08/2000x1325_q95.jpg"
#        ]


