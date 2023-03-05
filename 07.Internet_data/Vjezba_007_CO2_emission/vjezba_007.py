import requests
from bs4 import BeautifulSoup

URL ="https://www.worldometers.info/world-population/"

response = requests.get(URL)
population_page = BeautifulSoup(response.content, "html.parser")


