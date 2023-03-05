import requests
from bs4 import BeautifulSoup

page = 1
i = 1
books = {}
while page != 3:
    response = requests.get(f"http://books.toscrape.com/catalogue/category/books/mystery_3/page-{page}.html")

    data = BeautifulSoup(response.content, "html.parser")

    price_selector = ".price_color"
    heading_selector = ".product_pod h3 a"
    rating_selector = ".star-rating"

    price_selectors = data.select(price_selector)
    heading_selectors = data.select(heading_selector)
    rating_selectors = data.select(rating_selector)

    for price, heading, rating in zip(price_selectors, heading_selectors, rating_selectors):
        if rating.attrs['class'][1] == "One":
            books[i] = {
            "Price": price.get_text().replace("£", ""),
            "Heading": heading.get_text(),
            "Rating": "One"
        }
            i += 1
        elif rating.attrs['class'][1] == "Two":
            books[i] = {
            "Price": price.get_text().replace("£", ""),
            "Heading": heading.get_text(),
            "Rating": "Two"
        }
            i += 1
        elif rating.attrs['class'][1] == "Three":
            books[i] = {
            "Price": price.get_text().replace("£", ""),
            "Heading": heading.get_text(),
            "Rating": "Three"
        }
            i += 1
        elif rating.attrs['class'][1] == "Four":
            books[i] = {
            "Price": price.get_text().replace("£", ""),
            "Heading": heading.get_text(),
            "Rating": "Four"
        }
            i += 1
        elif rating.attrs['class'][1] == "Five":
            books[i] = {
            "Price": price.get_text().replace("£", ""),
            "Heading": heading.get_text(),
            "Rating": "Five"
        }
            i += 1

    page += 1
    
# for k, v in books.items():
#     print(f"{k}: Price {v['Price']}\nHeading: {v['Heading']}\nRating: {v['Rating']}")

most_expensive = 0
cheapest = 99999999999999
for k, v in books.items():
    if float(v['Price']) > most_expensive:
        most_expensive = float(v['Price'])
        most_expensive_book = k
    
    if float(v['Price']) < cheapest:
        cheapest = float(v['Price'])
        cheapest_book = k

print(f"Cheapest book is:\n{cheapest_book}: Price: {books[cheapest_book]['Price']}, Heading: {books[cheapest_book]['Heading']}, Star rating: {books[cheapest_book]['Rating']}\n")
print(f"Most expensive book is:\n{most_expensive_book}: Price: {books[most_expensive_book]['Price']}, Heading: {books[most_expensive_book]['Heading']}, Star rating: {books[most_expensive_book]['Rating']}")

try:
    with open("7.Internet_data/Vjezba_006_webshop_books/Books.txt", "a") as file_writer:
        file_writer.write(f"Cheapest book is:\n{cheapest_book}: Price: {books[cheapest_book]['Price']}, Heading: {books[cheapest_book]['Heading']}, Star rating: {books[cheapest_book]['Rating']}\n")
        file_writer.write(f"Most expensive book is:\n{most_expensive_book}: Price: {books[most_expensive_book]['Price']}, Heading: {books[most_expensive_book]['Heading']}, Star rating: {books[most_expensive_book]['Rating']}")
except Exception as e:
    print(e)