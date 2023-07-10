# Import the required modules
import requests
from bs4 import BeautifulSoup
import pandas as pd


url = "https://finance.yahoo.com/quote/AAPL/history?p=AAPL"


response = requests.get(url)

print(response.text)
# soup = BeautifulSoup(response.text, "html.parser")

# table = soup.find("table", class_="W(100%) M(0)")
# print(table)

# data = []
# rows = table.find_all("tr")


