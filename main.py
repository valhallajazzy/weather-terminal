import requests
def weather_forecast():
    urls = [
        'https://wttr.in/london?lang=ru&M&m&n&q&T',
        'https://wttr.in/череповец?lang=ru&M&m&n&q&T',
        'https://wttr.in/svo?lang=ru&M&m&n&q&T'
    ]
    location = input('Введите цифру для выбора локации прогноза погоды:'
            '\n 0 - London'
            '\n 1 - Cherepovets'
            '\n 2 - Аэропорт Шереметьево'
            '\n Ввод: ',
        )
    response = requests.get(f'{urls[int(location)]}')
    return print(response.text)