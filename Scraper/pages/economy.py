import requests
from bs4 import BeautifulSoup

url = 'https://www.nsi.bg/en/content/4011/unemployed-and-unemployment-rates-national-level-statistical-regions-districts'

def parse_soup(url):
    """
    Sends a GET request to the given URL and returns a BeautifulSoup object.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup

def get_areas_unemployement():
    """
    Retrieves the unemployment values for different areas.
    """
    soup = parse_soup(url)

    table = soup.find_all('table', class_='nsit3')[8]
    areas = table.find_all('td', class_='left_top')

    values = []
    for area in areas:
        values.append(area.find_next_sibling('td'))
    
    areas_dict = {}

    for i in range(len(areas)):
        # Clean up the text and convert to integer
        values[i] = values[i].text.replace('(', '').replace(')', '')
        areas_dict[areas[i].text] = int(float(values[i]) * 1000)
    
    areas = list(areas_dict.keys())
    areas.sort()
    areas_dict = {k: areas_dict[k] for k in areas}

    return list(areas_dict.values())


