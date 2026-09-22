"""
scraper.py
Scrapes the first 20 books from books.toscrape.com (Phase 1)
and loads them straight into books.db via BookDatabaseManager.
Pattern based on O1_basics.py (BeautifulSoup + requests).
"""

import requests
from bs4 import BeautifulSoup
from database import BookDatabaseManager

URL = "http://books.toscrape.com/"

RATING_MAP = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}


def scrape_first_20_books():
	response = requests.get(URL)
	response.raise_for_status()
	soup = BeautifulSoup(response.text, "html.parser")
	articles = soup.find_all("article", class_="product_pod")[:20]

	books = []
	for article in articles:
		title = article.find("h3").find("a")["title"].strip()
		price_text = article.find("p", class_="price_color").text.strip()
		price = float(price_text.replace("£", "").replace("Â", ""))
		in_stock = article.find("p", class_="instock availability").text.strip()
		rating_word = article.find("p", class_="star-rating")["class"][1]
		rating = RATING_MAP.get(rating_word, 0)
		books.append((title, price, in_stock, rating))
	return books


if __name__ == "__main__":
	db = BookDatabaseManager("books.db")
	books = scrape_first_20_books()
	db.insert_many(books)
	print(f"✓ Scraped and inserted {len(books)} books into books.db")
	db.close()
