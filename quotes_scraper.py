import requests
from bs4 import BeautifulSoup
import csv

def run_scraper():
    url = "https://quotes.toscrape.com"

    print(f"Connecting to {url}...")

    # Downloading the page
    response = requests.get(url)

    # Parsing the HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Finding the data
    quotes_data = []
    quotes = soup.find_all("div", class_="quote")
    # On this site, each quote is in a <div class= "quote">
    # Quotes contains a list in which each element is the
    # code for a different quote

    for q in quotes:
        text = q.find("span", class_="text").text
        author = q.find("small", class_="author").text

        # Saving each Quote and Author into a dictionary within quotes_data(list)
        quotes_data.append({"Quote": text, "Author": author})

    # Save data in CSV

    filename = "quotes.csv"
    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["Quote", "Author"])
        writer.writeheader()
        writer.writerows(quotes_data)

    print(f"\nSuccess! Saved {len(quotes_data)} quotes to {filename}.")

if __name__ == "__main__":
    run_scraper()
