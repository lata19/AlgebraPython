import urllib.request
import urllib.parse

# Adresa koju zelimo otvoriti
URL = "https://www.algebra.hr"

# objekt koji predstavlja konekciju prema adresi
konekcija = urllib.request.urlopen(URL)

# Citanje i dekodiranje sadrzaja koristeci konekciju
stranica = konekcija.read().decode()

print(stranica)

