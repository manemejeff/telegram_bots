import requests

from weather_bot.config import API_KEY
from weather_bot.config import RU_LANG_ID


def get_current_weather():
    try:
        req_url = 'http://api.openweathermap.org/data/2.5/weather?q=Samara,ru&appid={0}&units=metric&lang=ru'.format(
            API_KEY)
        r = requests.get(req_url)
        print(r.status_code)
        json_obj = r.json()
        cur_temp = json_obj['main']['temp']
        feels_like = json_obj['main']['feels_like']
        min_temp = json_obj['main']['temp_min']
        max_temp = json_obj['main']['temp_max']
        description = json_obj['weather'][0]['description']

        return 'В Самаре {0}.\nТекущая температура {1}.\nОщущается как {2}.\n' \
               'Минимальная температура {3}.\nМаксимальная температура {4}.'.format(description, cur_temp, feels_like,
                                                                                    min_temp, max_temp)
    except Exception as e:
        return 'Статус {0}, Ошибка {1}'.format(r.status_code, e)


def get_forecast_weather():
    try:
        req_url = 'http://api.openweathermap.org/data/2.5/forecast?q=Samara,ru&appid={0}&units=metric&lang=ru'.format(
            API_KEY)
        r = requests.get(req_url)
        json_obj = r.json()
        txt = ''
        for item in json_obj['list']:
            temp = item['main']['temp']
            date = item['dt_txt']
            description = item['weather'][0]['description']
            txt = txt + '{0}. Погода {1}. Температура {2}.\n'.format(date, description, temp)
        return txt
    except Exception as e:
        return 'Статус {0}, Ошибка {1}'.format(r.status_code, e)
