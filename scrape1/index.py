# import libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd
from io import StringIO
import json
import re
import csv

# # define the yahoo finance url
# # symbol = 'TSLA'
# symbol = 'AAPL'
#  # Replace with the desired stock symbol
# #url ='https://finance.yahoo.com/quote/{symbol}/financials?p={symbol}'
# url = f'https://finance.yahoo.com/quote/{symbol}'

# #send a get request to the url to retrieve the html content
# response = requests.get(url)
# html_content = response.text

# #create a beautifulsoup object to parse the html
# soup = BeautifulSoup(html_content, 'html.parser')

# # # extract the desired stock
# # price_element = soup.find('span', class_='Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)')
# # stock_price = price_element.text

# # data = {'Stock Symbol': [symbol], 'Stock Price': [stock_price]}
# # df = pd.DataFrame(data)

# print(response)

url_stats = "https://finance.yahoo.com/quote/{}/key-statistics?p={}"
url_profile = "https://finance.yahoo.com/quote/{}/profile?p={}"
url_financials = "https://finance.yahoo.com/quote/{}/financials?p={}"

stock = "F"

response = requests.get(url_financials.format(stock, stock))

soup = BeautifulSoup(response.text, "html.parser")

pattern = re.compile(r"\s--\sData\s--\s")
script_data = soup.find("script", text=pattern).contents[0]

#beginning
script_data[:500]

# end
script_data[-500:]