import os
import requests

import auxiliary_scripts
import requests_api


def main():
    folder = 'images'
    arg_type = str
    arg_default = '5eb87d47ffd86e000604b38a'
    arg_help = 'id запуска(по умолчанию: 5eb87d47ffd86e000604b38a)'
    url = (
        f'https://api.spacexdata.com/v5/launches/'
        f'{auxiliary_scripts.get_arguments(arg_type, arg_default, arg_help)}'
    )

    params = None

    try:
        spacex_images = requests_api.get_images_url(url, params)
    except requests.exceptions.RequestException as e:
        print(f'Ошибка загрузки списка изображений: {e}')

    if spacex_images:
        os.makedirs(folder, exist_ok=True)

    links = spacex_images.get('links', {})
    flickr = links.get('flickr', {})
    flickr_images = flickr.get('original', [])

    for index, img_url in enumerate(flickr_images):
        filename = os.path.join(folder, f'spacex_{index}.jpg')
        try:
            auxiliary_scripts.save_image(filename, img_url)
        except requests.exceptions.RequestException as e:
            print(f'Ошибка загрузки изображения: {e}')


if __name__ == '__main__':
    main()
