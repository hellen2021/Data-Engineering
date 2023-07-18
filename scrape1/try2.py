# import libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd

from bs4 import BeautifulSoup

html = """
<html>
<body>
    <div class="container">
        <p class="text">Hello, World!</p>
        <p class="text">This is a paragraph.</p>
        <p class="text">Another paragraph.</p>
    </div>
</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")

# Using find
first_paragraph = soup.find("p")
print("First paragraph ", first_paragraph.text)  # Output: <p class="text">Hello, World!</p>

# Using find_all
all_paragraphs = soup.find_all("p")
for paragraph in all_paragraphs:
    print(paragraph.text)  # Output: <p class="text">Hello, World!</p>, <p class="text">This is a paragraph.</p>, <p class="text">Another paragraph.</p>
