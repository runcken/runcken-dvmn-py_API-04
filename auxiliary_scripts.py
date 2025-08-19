import argparse
import datetime


def get_arguments():
    parser = argparse.ArgumentParser(
        description='Получение фото SpaceX и NASA'
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

    args = parser.parse_args()
    id_launch = args.id_launch
    days = args.days
    return id_launch, days


def get_download_date_from(days):
    today = datetime.date.today()
    download_date = today - datetime.timedelta(days)
    return download_date
