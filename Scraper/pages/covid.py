import requests
from bs4 import BeautifulSoup

url = 'https://coronavirus.bg/bg/statistika'

areas = [
"BLG",
"BGS",
"VAR",
"VTR",
"VID",
"VRC",
"GAB",
"DOB",
"KRZ",
"KNL",
"LOV",
"MON",
"PAZ",
"PER",
"PVN",
"PDV",
"RAZ",
"RSE",
"SLS",
"SLV",
"SML",
"SFO",
"SOF",
"SZR", 
"TGV",
"HKV",
"SHU",
"JAM"
]

def parse_soup(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    return soup

def get_elements_by_table_index(index):
    soup = parse_soup(url)

    tables = soup.find_all('table', class_='table')

    elements = tables[index].find_all('td', attrs={'style': 'text-align: right;'})

    return elements

def get_new_cases():
    table = get_elements_by_table_index(3)

    new_cases = []

    for i in range(1, len(table), 2):
        new_cases.append(table[i].text)
    
    return new_cases

def get_vaccines():
    table = get_elements_by_table_index(5)

    vaccines = []

    for i in range(6, len(table), 9):
        vaccines.append(table[i].text)
    
    return vaccines
