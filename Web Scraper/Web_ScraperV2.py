import requests
import json
from bs4 import BeautifulSoup

response = requests.get("https://quotes.toscrape.com")

print(response.status_code)
# print(response.text)

soup = BeautifulSoup(response.text, "html.parser")

print(soup.title.text)

quotes = soup.find_all(class_="quote")

quotes_data = []

for quote in quotes:
    text = quote.find(class_="text").text
    author = quote.find(class_="author").text

    quote_info = {
        "Quote" : text,
        "Author" : author
    }
    quotes_data.append(quote_info)
    print(text)
    print(f" -> {author}")
    print()

with open("quotes.json", "w")as f:
    json.dump(quotes_data, f, indent=4)