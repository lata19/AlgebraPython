import requests
from bs4 import BeautifulSoup


response = requests.get("http://books.toscrape.com")

data = BeautifulSoup(response.content, "html.parser")

price_selector = ".price_color"
heading_selector = ".product_pod h3 a"
rating_selector = ".star-rating"

data.select(price_selector)

