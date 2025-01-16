
import requests
import json

from bs4 import BeautifulSoup as Bs


class WetherParser:

    def __init__(self):
        self.base_url = 'https://world-weather.ru/pogoda/russia/saint_petersburg/7days/'
        self.html = None
        self.html_russia = None
        self.rrussia_base_url = 'https://spys.one/free-proxy-list/RU/'
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 YaBrowser/24.12.0.0 Safari/537.36'}
        self.weather_list = []
        self.weather_dict = {}
        self.all_list = []
        self.all_data = {}
        self.data = []


    def get_html(self):
        response = requests.get(self.base_url, headers=self.headers)
        if response.status_code != 200:
            print(f'Error!!!{response.status_code}')
            print(response.status_code)
        else:
            html = response.text
            self.html = html
            #print(response.text, self.html)


    def parse_page(self):

        time_of_day_list = []
        #if self.get_html():
        soup = Bs(self.html, 'html.parser')
        data = soup.find_all('div', class_='weather-short')
        test = []
        for j in range(len(data)):
            test.append(data[j].find('span').text)
            items_today = data[j].find_all('tr')

            for item in items_today:

                time_of_day_list.append(item.find('td', class_='weather-day').text)

                item_dict = {
                    'weather_quality': item.find('td', class_='weather-temperature').find('div').get('title'),
                    'temperature': item.find('td', class_='weather-temperature').find('span').text,
                    'feel_temperature': item.find('td', class_='weather-feeling').text,
                    'weather-probability': item.find('td', class_='weather-probability').text,
                    'weather-pressure': item.find('td', class_='weather-pressure').text,
                    'weather-wind': item.find('td', class_='weather-wind').find('span').get('title'),
                    'wind_direction_in_degrees': item.find('td', class_='weather-wind').find('span').findNext('span').text,
                    'weather-humidity': item.find('td', class_='weather-humidity').text,
                    'sunrise_time': data[j].find('div', class_='sun-box').find('div').text,
                    'sun_set_time': data[j].findNext('div', class_='sun-box').find('div').findNext('div').text
                }
                self.weather_list.append(item_dict)

        for i in  range(len(self.weather_list)):
            weather_dict = {time_of_day_list[i]: self.weather_list[i]}
            self.all_list.append(weather_dict)

        self.data = [self.all_list[i:i + 4] for i in range(0, len(self.all_list), 4)]

        for par in range(len(self.data)):
            self.all_data[test[par]] = self.data[par]

        return self.all_data


    def add_data_to_file(self):
        with open('RESULT.json', 'w', encoding='utf-8') as file:
            json.dump(self.all_data, file, ensure_ascii=False, indent=2)


parser_weather = WetherParser()
parser_weather.get_html()

parser_weather.parse_page()
#print(parser_weather.all_data)

parser_weather.add_data_to_file()


'''
получить первый второй и четвертый столбцы 

отдельно получить российские Proxy (https://spys.one/free-proxy-list/RU/) ip, proxy, latency

'''