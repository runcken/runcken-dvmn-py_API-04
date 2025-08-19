import os
import requests

import auxiliary_scripts
import requests_api


def main():
    folder = 'images'
    url = (
        f'https://api.spacexdata.com/v5/launches/'
        f'{auxiliary_scripts.get_arguments()[0]}'
    )
    params = None

    spacex_images = requests_api.get_images_url(url, params)
    if spacex_images:
        os.makedirs(folder, exist_ok=True)

    links = spacex_images.get('links', {})
    flickr = links.get('flickr', {})
    flickr_images = flickr.get('original', [])

    for i, img_url in enumerate(flickr_images):
        img_response = requests.get(img_url)
        filename = os.path.join(folder, f'spacex_{i}.jpg')
        with open(filename, 'wb') as file:
            file.write(img_response.content)


if __name__ == '__main__':
    main()
