# Прогноз погоды

Скрипт позволяет получить прогноз погоды через терминал  
ссылаясь на сервис [wttr.in](https://wttr.in/) по 3 локациям:

* Лондон
* Череповец
* Аэропорт Шереметьево (SVO)

## Устновка и активация виртуального окружения(env)

В терминале, в корневой папке проекта создаем вирутальное окружение:

```console
$ virtualenv venv
$ source venv/bin/activate
```

## Установка библиотек из requirements.txt

В терминале, в корневой папке проекта устанавливаем библиотеки:

```console
$ python -m pip install -r requirements.txt
```

Библиотеки официально поддерживают Python 3.5+

## Запуск скрипта

В терминале, в корневой папке проекта запускаем скрипт:

```console
$ python3 main.py
```

Пример запуска скрипта:
![Screenshot](https://github.com/valhallajazzy/weather-terminal/blob/main/%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D1%80_%D0%B7%D0%B0%D0%BF%D1%83%D1%81%D0%BA%D0%B0_%D1%81%D0%BA%D1%80%D0%B8%D0%BF%D1%82%D0%B0.png)
