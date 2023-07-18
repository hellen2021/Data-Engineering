from bs4 import BeautifulSoup
import requests

url = 'https://finance.yahoo.com/etfs'

response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, 'html.parser')
print(soup)