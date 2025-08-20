import argparse
import datetime
import requests


def get_arguments(arg_type, arg_default, arg_help):
    parser = argparse.ArgumentParser(
        description='отправка изображений в телеграм канал'
    )

    parser.add_argument(
        '--arg',
        type=arg_type,
        default=arg_default,
        help=arg_help
    )

    args = parser.parse_args()
    arg = args.arg
    return arg


def get_download_date_from(days):
    today = datetime.date.today()
    download_date = today - datetime.timedelta(days)
    return download_date


def save_image(filename, img_url):
    img_response = requests.get(img_url)
    img_response.raise_for_status()
    with open(filename, 'wb') as file:
        file.write(img_response.content)
