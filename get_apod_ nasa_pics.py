import os
import requests
import datetime
from environs import Env


env = Env()
env.read_env()


def fetch_apod_nasa(folder, apod_url, api_key_nasa, target_date):
    params={
            'api_key': api_key_nasa,
            'start_date': target_date
            }
    try:
        response = requests.get(apod_url, params=params)
        apod_photos = response.json()

    except requests.exceptions.RequestException as e:
        print(f"Ошибка при скачивании изображения: {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

    if apod_photos:
        os.makedirs(folder, exist_ok=True)
    image_urls = []

    for apod_photo in apod_photos:
        if apod_photo.get('media_type') == 'image':
            image_urls.append(apod_photo['url'])

    for url in image_urls:
        image_name = url.split('/')[-1]
        filename = os.path.join(folder, f'apod_{image_name}')
        img_response = requests.get(url)
        with open(filename, 'wb') as file:
            file.write(img_response.content)


def main():
    folder = 'images'
    api_key_nasa = env.str('API_KEY_NASA')
    today = datetime.date.today()
    target_date = today - datetime.timedelta(days=10)
    apod_url = 'https://api.nasa.gov/planetary/apod'
    fetch_apod_nasa(folder, apod_url, api_key_nasa, target_date)


if __name__ == '__main__':
    main()
