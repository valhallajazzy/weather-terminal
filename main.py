import logging
import requests
from requests import HTTPError


def main():
    payload = {"location": "", "lang": "ru", "M": "", "m": "", "n": "", "q": "", "T": ""}
    locations = ['Лондон', 'Череповец', 'svo']
    for location in locations:
        response = requests.get(f'https://wttr.in/{location}3463gg', params=payload)
        response.raise_for_status()
        print(response.text)


if __name__ == '__main__':
    main()
