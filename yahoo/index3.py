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
# if table is not None:
#     data = []
#     rows = table.find_all("tr")

#     for row in rows:
#         cols = row.find_all("td")
#         if len(cols) == 7:  # Check if it's a valid row
#             row_data = [col.text.strip() for col in cols]
#             data.append(row_data)

#     df = pd.DataFrame(data, columns=["Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"])
#     print(df)
# else:
#     print("Table not found.")
