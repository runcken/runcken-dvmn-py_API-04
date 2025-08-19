import argparse
import datetime


def get_arguments():
    parser = argparse.ArgumentParser(
        description='отправка изображений в телеграм канал'
    )

    parser.add_argument(
        '--id_launch',
        type=str,
        default='5eb87d47ffd86e000604b38a',
        help='id запуска(по умолчанию: 5eb87d47ffd86e000604b38a)'
    )

    parser.add_argument(
        '--days',
        type=str,
        default=40,
        help='количество дней для загрузки(по умолчанию: 40)'
    )

    parser.add_argument(
        '--seconds',
        type=int,
        default=20,
        help='задержка в секундах(по умолчанию: 20)'
    )

    parser.add_argument(
        '--filename',
        type=str,
        default='spacex_0.jpg',
        help='файл для отправки(по умолчанию: spacex_0.jpg)'
    )

    args = parser.parse_args()
    id_launch = args.id_launch
    days = args.days
    seconds = args.seconds
    filename = args.filename
    return id_launch, days, seconds, filename


def get_download_date_from(days):
    today = datetime.date.today()
    download_date = today - datetime.timedelta(days)
    return download_date
