from bs4 import BeautifulSoup

with open("Sample.html", "r") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

print(soup)

headlines = soup.find_all("h1")

print(headlines)

for headline in headlines:
    print(headline.text)

# print(soup.find_all("div"))

articles = soup.find_all(class_="article")

for article in articles:
    print(article.text)