import requests


def get_images_url(url, params):
    response = requests.get(url, params=params)
    response.raise_for_status()
    image_response = response.json()
    return image_response
