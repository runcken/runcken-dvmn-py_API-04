import os
import requests
from environs import Env

import auxiliary_scripts
import requests_api


env = Env()
env.read_env()


def main():
    folder = 'images'
    api_key_nasa = env.str('API_KEY_NASA')
    days = auxiliary_scripts.get_arguments()[1]
    target_date = auxiliary_scripts.get_download_date_from(days)
    url = f'https://epic.gsfc.nasa.gov/api/enhanced/date/{target_date}'
    params = {'api_key': api_key_nasa}

    epic_images = requests_api.get_images_url(url, params)

    if epic_images:
        os.makedirs(folder, exist_ok=True)
    last_epic_images = epic_images[:5]

    for idx, image in enumerate(last_epic_images):
        image_name = image['image'] + '.png'
        date_str = target_date.strftime('%Y-%m-%d')
        formatted_date = date_str.replace('-', '/')
        image_url = (
            f'https://epic.gsfc.nasa.gov/archive/enhanced'
            f'/{formatted_date}/png/{image_name}'
        )
        img_response = requests.get(image_url)
        with open(os.path.join(folder, image_name), 'wb') as file:
            file.write(img_response.content)


if __name__ == '__main__':
    main()
