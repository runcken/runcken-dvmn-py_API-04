import os
import telegram
import time
import random
from environs import Env

import auxiliary_scripts


def main():
    env = Env()
    env.read_env()

    chat_id = env.str('TG_CHANNEL')
    folder = 'images'
    arg_type = int
    arg_default = 1440
    arg_help = 'задержка в секундах(по умолчанию: 14400)'

    bot = telegram.Bot(token=env.str('TG_TOKEN'))
    image_files = []

    while not image_files:
        image_files = [
            file for file in os.listdir(folder)
            if file.lower().endswith(('.png', 'jpg', 'jpeg', 'gif'))
        ]
        continue

    random.shuffle(image_files)
    starting_arg = auxiliary_scripts.get_arguments(
                arg_type, arg_default, arg_help)

    while True:
        for idx, image_file in enumerate(image_files):
            image_path = os.path.join(folder, image_file)
            with open(image_path, 'rb') as photo:
                bot.send_photo(chat_id=chat_id, photo=photo)
            time.sleep(starting_arg)
            if not idx:
                random.shuffle(image_files)
                idx = 0


if __name__ == '__main__':
    main()
