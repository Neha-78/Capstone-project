"""FastAPI app for serving books from the local SQLite database."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from database import BookDatabaseManager


app = FastAPI(title="Book API")

app.add_middleware(
	CORSMiddleware,
	allow_origins=["*"],
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)


@app.get("/")
def read_root():
	return {"message": "Book API is running"}


@app.get("/books")
def get_books():
	db = BookDatabaseManager("books.db")
	try:
		rows = db.get_all_books()
		return [
			{
				"id": book_id,
				"title": title,
				"price": price,
				"in_stock": in_stock,
				"rating": rating,
			}
			for book_id, title, price, in_stock, rating in rows
		]
	finally:
		db.close()


if __name__ == "__main__":
	uvicorn.run(app, host="127.0.0.1", port=8000)