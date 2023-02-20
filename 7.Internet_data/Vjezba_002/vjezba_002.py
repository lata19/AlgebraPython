import requests

URL = "https://www.algebra.hr"
response = requests.get(URL)
print(response.status_code)
print(response.content)
print(response.headers)
print(response.text)