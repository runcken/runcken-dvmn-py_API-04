import os
import telegram
import time
import random
from environs import Env

import auxiliary_scripts


env = Env()
env.read_env()

chat_id = '@cosmo_runcken'
folder = 'images'


def main():
    bot = telegram.Bot(token=env.str('TG_TOKEN'))
    image_files = []

    while not image_files:
        image_files = [
            file for file in os.listdir(folder)
            if file.lower().endswith(('.png', 'jpg', 'jpeg', 'gif'))
        ]
        continue

    random.shuffle(image_files)
    index = 0

    while True:
        image_path = os.path.join(folder, image_files[index])
        with open(image_path, 'rb') as photo:
            bot.send_photo(chat_id=chat_id, photo=photo)
        index += 1
        time.sleep(auxiliary_scripts.get_arguments()[2])

        if index >= len(image_files):
            random.shuffle(image_files)
            index = 0


if __name__ == '__main__':
    main()
