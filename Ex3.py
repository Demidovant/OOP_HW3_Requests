import requests
from datetime import datetime, timedelta


def get_questions(fromdate=0, tag=''):
    URL = 'https://api.stackexchange.com/2.3/questions'
    params = {'site': 'stackoverflow', 'fromdate': int(fromdate), 'tagged': tag, 'pagesize': 100}
    response = requests.get(URL, params=params)

    for item in response.json()['items']:
        print(item['title'])
    # print(len(response.json()['items']))


def get_unixtime_x_daysago(x):
    """Результат - Unixtime X дней назад в 00:00:00"""
    tergettime = datetime.now() - timedelta(days=x)
    return datetime(tergettime.year, tergettime.month, tergettime.day).timestamp()


if __name__ == '__main__':
    fromdate = get_unixtime_x_daysago(2)
    tag = 'python'
    # tag = 'python; java'

    get_questions(fromdate, tag=tag)
    # get_questions(tag=tag)
    # get_questions(fromdate)
    # get_questions()
