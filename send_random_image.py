import os
import telegram
import random
from environs import Env

import auxiliary_scripts


env = Env()
env.read_env()


def main():
    chat_id = env.str('TG_CHANNEL')
    folder = 'images'
    files = os.listdir(folder)

    if files:
        random_file = random.choice(files)
    bot = telegram.Bot(token=env.str('TG_TOKEN'))
    target_file = auxiliary_scripts.get_arguments()[3]

    if target_file:
        with open(os.path.join(folder, target_file), 'rb') as photo:
            bot.send_photo(chat_id=chat_id, photo=photo)
    else:
        with open(os.path.join(folder, random_file), 'rb') as photo:
            bot.send_photo(chat_id=chat_id, photo=photo)


if __name__ == '__main__':
    main()
