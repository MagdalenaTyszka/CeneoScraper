import requests
from bs4 import BeautifulSoup

url = "https://www.ceneo.pl/61777651#tab=reviews"
response = requests.get(url)

page_dom = BeautifulSoup(response.text, 'html.parser')

print(page_dom.prettify())
