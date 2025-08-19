import requests


def get_images_url(url, params):
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        images_url = response.json()
    except requests.exceptions.RequestException as e:
        print(f'Ошибка при скачивании изображения: {e}')
    except Exception as e:
        print(f'Произошла ошибка: {e}')
    return images_url
