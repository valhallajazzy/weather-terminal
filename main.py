import logging
import requests
from requests import HTTPError


def main():
    payload = {"location": "", "lang": "ru", "M": "", "m": "", "n": "", "q": "", "T": ""}
    locations = ['Лондон', 'Череповец', 'svo']
    for location in locations:
        try:
            response = requests.get(f'https://wttr.in/{location}', params=payload)
            response.raise_for_status()
        except HTTPError:
            logging.exception('Ошибка соединения с сервером')
    print(response.text)


if __name__ == '__main__':
    main()
