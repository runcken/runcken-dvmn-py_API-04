import os
import requests


def fetch_spacex_last_launch(spacex_url):
    try:
        response = requests.get(spacex_url)
        response.raise_for_status()
        spacex_photos = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при скачивании списка фото: {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

    flickr_images = spacex_photos.get('links', {}).get('flickr', {}).get('original', [])

    if flickr_images:
        os.makedirs('images', exist_ok=True)
        
    for i, img_url in enumerate(flickr_images):
        img_data = requests.get(img_url).content
        filename = f'images/spacex_{i}.jpg'
        with open(filename, 'wb') as file:
            file.write(img_data)


def main():
    spacex_url = 'https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a'
    fetch_spacex_last_launch(spacex_url)


if __name__ == '__main__':
    main()
