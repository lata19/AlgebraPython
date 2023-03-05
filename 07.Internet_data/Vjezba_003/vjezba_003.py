import requests
from bs4 import BeautifulSoup

URL = "https://www.algebra.hr"
response = requests.get(URL)

page = BeautifulSoup(response.content)

paragraphs = page.find_all("p")

for p in paragraphs:
    print(p)