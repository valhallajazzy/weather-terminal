import requests
def main():
    payload = {"location": "", "lang": "ru", "M": "", "m": "", "n": "", "q": "", "T": ""}
    locations = ['Лондон', 'Череповец', 'svo']
    for location in locations:
        response = requests.get(f'https://wttr.in/{location}', params=payload)
        print(response.text)

if __name__ == '__main__':
    main()

