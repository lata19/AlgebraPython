import requests
from bs4 import BeautifulSoup

URL_COVID = "https://www.worldometers.info/coronavirus" 

response = requests.get(URL_COVID)
covid_page = BeautifulSoup(response.content, "html.parser")


data = covid_page.find_all("div", id="maincounter-wrap")

# print(data)

# coronavirus_cases = data[0]
# heading = coronavirus_cases.find("h1").get_text()
# cases_number = coronavirus_cases.find("span").get_text()
# print(heading, cases_number)

# coronavirus_deaths = data[1]
# heading = coronavirus_deaths.find("h1").get_text()
# deaths_number = coronavirus_deaths.find("span").get_text()
# print(heading, deaths_number)

# coronavirus_recovers = data[2]
# heading = coronavirus_recovers.find("h1").get_text()
# recovers_number = coronavirus_recovers.find("span").get_text()
# print(heading, recovers_number)

for item in data:
    heading = item.find("h1").get_text()
    cases_number = item.find("span").get_text()
    print(heading, cases_number)