import os
import telegram
import random
from environs import Env

import auxiliary_scripts


def main():
    env = Env()
    env.read_env()

    chat_id = env.str('TG_CHANNEL')
    folder = 'images'
    files = os.listdir(folder)

    bot = telegram.Bot(token=env.str('TG_TOKEN'))
    arg_type = str
    arg_default = random.choice(files)
    arg_help = 'файл для отправки(по умолчанию: spacex_0.jpg)'
    file = auxiliary_scripts.get_arguments(arg_type, arg_default, arg_help)

    with open(os.path.join(folder, file), 'rb') as photo:
        bot.send_photo(chat_id=chat_id, photo=photo)


if __name__ == '__main__':
    main()
