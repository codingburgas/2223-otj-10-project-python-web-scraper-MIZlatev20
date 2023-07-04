import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0'}

areas = [
    'blagoevgrad/43813',
    'burgas/47424',
    'varna/51536',
    'veliko-tarnovo/46650',
    'vidin/46734',
    'vratsa/46791',
    'gabrovo/43437',
    'dobrich/43349',
    'kardzhali/43604',
    'kyustendil/43814',
    'lovech/43882',
    'montana/44409',
    'pazardzhik/44947',
    'pernik/45093',
    'pleven/45254',
    'plovdiv/49959',
    'razgrad/45405',
    'ruse/50167',
    'silistra/45981',
    'sliven/46032',
    'smolyan/46072',
    'sofia-airport/1268_poi/',
    'sofia/51097',
    'stara-zagora/46322',
    'targovishte/46514',
    'haskovo/48599',
    'shumen/45926',
    'yambol/46846'
]

def parse_soup(url):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    return soup

def get_temp_by_area(index):
    area_id = areas[index].split('/')[1]
    formatted_url = f'https://www.accuweather.com/en/bg/{areas[index]}/afternoon-weather-forecast/{area_id}'

    soup = parse_soup(formatted_url)

    temperature = soup.find('div', class_='temperature').text

    return temperature.strip()[:-1]

def get_humidity_by_area(index):
    area_id = areas[index].split('/')[1]
    formatted_url = f'https://www.accuweather.com/en/bg/{areas[index]}/afternoon-weather-forecast/{area_id}'

    soup = parse_soup(formatted_url)

    panels = soup.find('div', class_='panels')
    humidity = panels.find_all('span', class_='value')[2].text

    return humidity[:-1]

def get_aq_by_area(index):
    area_id = areas[index].split('/')[1]
    formatted_url = f'https://www.accuweather.com/en/bg/{areas[index]}/weather-forecast/{area_id}'

    soup = parse_soup(formatted_url)

    aq = soup.find('div', class_='aq-number').text

    return aq.strip()

def get_temperatures():
    return [get_temp_by_area(i) for i in range(len(areas))]

def get_humidities():
    return [get_humidity_by_area(i) for i in range(len(areas))]

def get_aq():
    return [get_aq_by_area(i) for i in range(len(areas))]
