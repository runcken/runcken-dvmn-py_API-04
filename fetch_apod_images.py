import os
import requests
from environs import Env

import auxiliary_scripts
import requests_api


def main():
    env = Env()
    env.read_env()

    folder = 'images'
    api_key_nasa = env.str('API_KEY_NASA')
    url = 'https://api.nasa.gov/planetary/apod'
    arg_type = int
    arg_default = 10
    arg_help = 'количество дней для загрузки(по умолчанию: 10)'
    days = auxiliary_scripts.get_arguments(arg_type, arg_default, arg_help)
    params = {
            'api_key': api_key_nasa,
            'start_date': auxiliary_scripts.get_download_date_from(days)
    }

    try:
        apod_images = requests_api.get_images_url(url, params)
    except requests.exceptions.RequestException as e:
        print(f'Ошибка загрузки списка изображений: {e}')

    if apod_images:
        os.makedirs(folder, exist_ok=True)
    img_urls = []

    for apod_image in apod_images:
        img_urls.append(apod_image['url'])

    for img_url in img_urls:
        img_name = img_url.split('/')[-1]
        filename = os.path.join(folder, f'apod_{img_name}')
        try:
            auxiliary_scripts.save_image(filename, img_url)
        except requests.exceptions.RequestException as e:
            print(f'Ошибка загрузки изображения: {e}')


if __name__ == '__main__':
    main()
