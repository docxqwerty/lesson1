import requests

gps = {'sheremetievo': '55.96669, 37.41575',
       'cherepovec': '59.283333, 38.066666',
       'london': '51.889267, 0.262703'}


def get_weather(gps):
    for val in gps.values():
        url = f'https://wttr.in/{val}'
        try:
            r = requests.get(url)
            print(r.text)
        except Exception as E:
            print('Погода недоступна')


if __name__ == '__main__':
    get_weather(gps)
