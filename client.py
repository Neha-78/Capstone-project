import requests
import pandas as pd
import matplotlib.pyplot as plt

API_URL = "http://127.0.0.1:8000/books"


def fetch_books():
    response = requests.get(API_URL)
    response.raise_for_status()
    return response.json()


def main():
    books = fetch_books()
    df = pd.DataFrame(books)
    print(df)

    df.to_csv("exported_books.csv", index=False)
    print("✓ Exported to exported_books.csv")

    plt.figure(figsize=(8, 6))
    plt.scatter(df["price"], df["rating"], c="royalblue")
    plt.title("Book Price vs Rating")
    plt.xlabel("Price (£)")
    plt.ylabel("Rating (1-5)")
    plt.grid(True)
    plt.savefig("priceVSrating.png")
    print("✓ Saved plot to price_vs_rating.png")


if __name__ == "__main__":
    main()