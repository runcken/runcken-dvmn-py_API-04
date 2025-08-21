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
    arg_type = int
    arg_default = 40
    arg_help = 'количество дней для загрузки(по умолчанию: 40)'
    days = auxiliary_scripts.get_arguments(arg_type, arg_default, arg_help)
    target_date = auxiliary_scripts.get_download_date_from(days)
    url = f'https://epic.gsfc.nasa.gov/api/enhanced/date/{target_date}'
    params = {'api_key': api_key_nasa}

    try:
        epic_images = requests_api.get_images_url(url, params)
    except requests.exceptions.RequestException as e:
        print(f'Ошибка загрузки списка изображений: {e}')
    if epic_images:
        os.makedirs(folder, exist_ok=True)
    images_number = 5
    last_epic_images = epic_images[:images_number]

    for idx, image in enumerate(last_epic_images):
        img_name = f'{image['image']}.png'
        filename = os.path.join(folder, img_name)
        date_str = target_date.strftime('%Y/%m/%d')
        img_url = (
            f'https://epic.gsfc.nasa.gov/archive/enhanced'
            f'/{date_str}/png/{img_name}'
        )
        try:
            auxiliary_scripts.save_image(filename, img_url)
        except requests.exceptions.RequestException as e:
            print(f'Ошибка загрузки изображения: {e}')


if __name__ == '__main__':
    main()
