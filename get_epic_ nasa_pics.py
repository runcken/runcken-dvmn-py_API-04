nimport os
import requests
import datetime
from environs import Env


env = Env()
env.read_env()


def fetch_nasa_epic(target_date, folder, API_KEY_NASA, url):
    try:
        response = requests.get(url, params={'api_key': API_KEY_NASA})
        response.raise_for_status()
        photos = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при скачивании списка фото: {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

    if photos:
        os.makedirs(folder, exist_ok=True)
    some_photos = photos[:5]
    for idx, photo in enumerate(some_photos):
        image_name = photo['image'] + '.png'
        date_str = target_date.strftime('%Y-%m-%d')
        formatted_date = date_str.replace('-', '/')
        image_url = f'https://epic.gsfc.nasa.gov/archive/natural/{formatted_date}/png/{image_name}'
        img_data = requests.get(image_url).content
        with open(os.path.join(folder, image_name), 'wb') as file:
            file.write(img_data)


def main():
    API_KEY_NASA = env.str('API_KEY_NASA')
    today = datetime.date.today()
    target_date = today - datetime.timedelta(days=30)
    folder = 'images'
    url = f'https://epic.gsfc.nasa.gov/api/natural/date/{target_date}'
    fetch_nasa_epic(target_date, folder, API_KEY_NASA, url)


if __name__ == '__main__':
    main()
