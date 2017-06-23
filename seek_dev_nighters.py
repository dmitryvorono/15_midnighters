import requests
from datetime import datetime
from pytz import timezone
import pprint


def fetch_solution_attempts(page):
    request = requests.get('https://devman.org/api/challenges/solution_attempts/?page={0}'.format(page))
    if request.status_code == requests.codes.ok:
        return request.json()


def load_attempts(start_page):
    content = fetch_solution_attempts(start_page)
    if content is None:
        return
    yield content['records']
    number_of_pages = content['number_of_pages']
    for page in range(start_page + 1, number_of_pages + 1):
        content = fetch_solution_attempts(page)
        yield content['records']


def is_owl(attempt):
    if attempt['timestamp'] is None:
        return False
    client_tz = attempt['timezone']
    server_time = datetime.utcfromtimestamp(int(attempt['timestamp']))
    client_time = timezone(client_tz).fromutc(server_time)
    return client_time.hour == 0


def get_midnighters(attempts):
    return [attempt for attempt in attempts if is_owl(attempt)]


def print_midnighters(attempts):
    if attempts:
        pprint.pprint(attempts, indent=4)


if __name__ == '__main__':
    start_page = 1
    attempts_generator = load_attempts(start_page)
    for attempts in attempts_generator:
        print_midnighters(get_midnighters(attempts))
