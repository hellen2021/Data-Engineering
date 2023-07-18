import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the Yahoo Finance URL for the stock's historical data
symbol = 'AAPL'  # Replace with the desired stock symbol
url = f'https://finance.yahoo.com/quote/{symbol}/history'

# Send a GET request to the URL and retrieve the HTML content
response = requests.get(url)
html_content = response.text

# Create a BeautifulSoup object to parse the HTML
soup = BeautifulSoup(html_content, 'lxml')

table = soup.find('table', class_ = 'W(100%) M(0)')

# Extract the table headers
headers = table.find('thead').find_all('th')
column_names = [header.text for header in headers]

# Extract the table rows
rows = table.find('tbody').find_all('tr')

# Create an empty list to store the scraped data
data = []

# Iterate over the rows and extract the data
for row in rows:
    cells = row.find_all('td')
    row_data = [cell.text for cell in cells]
    data.append(row_data)

# Create a Pandas DataFrame using the scraped data
df = pd.DataFrame(data, columns=column_names)

# Display the scraped data
print(df)