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
    url = 'https://api.nasa.gov/planetary/apod'
    days = auxiliary_scripts.get_arguments()[1]
    params = {
            'api_key': api_key_nasa,
            'start_date': auxiliary_scripts.get_download_date_from(days)
    }

    apod_images = requests_api.get_images_url(url, params)

    if apod_images:
        os.makedirs(folder, exist_ok=True)
    image_urls = []

    for apod_image in apod_images:
        if apod_image.get('media_type') == 'image':
            image_urls.append(apod_image['url'])

    for image_url in image_urls:
        image_name = image_url.split('/')[-1]
        filename = os.path.join(folder, f'apod_{image_name}')
        img_response = requests.get(image_url)
        with open(filename, 'wb') as file:
            file.write(img_response.content)


if __name__ == '__main__':
    main()
