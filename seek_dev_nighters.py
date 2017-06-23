import requests
from datetime import datetime
from pytz import timezone
import pprint


def fetch_solution_attempts(page):
    request = requests.get('https://devman.org/api/challenges/solution_attempts/?page={0}'.format(page))
    if request.status_code == requests.codes.ok:
        return request.json()


def load_attempts(start_page, delta=1):
    page = start_page
    while True:
        content = fetch_solution_attempts(page)
        if content is None:
            break
        yield content['records']
        page += delta


def get_midnighters(attempts):
    def is_owl(attempt):
        if attempt['timestamp'] is None:
            return False
        client_tz = attempt['timezone']
        server_time = datetime.utcfromtimestamp(int(attempt['timestamp']))
        client_time = timezone(client_tz).fromutc(server_time)
        return client_time.hour == 0
    return list(filter(is_owl, attempts))


def print_midnighters(attempts):
    if attempts:
        pprint.pprint(attempts, indent=4)


if __name__ == '__main__':
    start_page = 1
    l = load_attempts(start_page)
    for i in l:
        print_midnighters(get_midnighters(i))
