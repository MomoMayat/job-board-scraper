# Python Web Scraper Practice

I built this to learn how to get data from websites automatically instead of copying and pasting it manually.
There are two scrapers. One scrapes quotes from https://quotes.toscrape.com and the other scrapes jobs from Indeed.

## What it does
* Goes to a website using the `requests` library.
* Uses `BeautifulSoup` to find specific parts of the page (like quotes and authors).
* Saves everything into a CSV file.

## What I learned
I wanted to learn:
1. How to use a virtual environment (`venv`) to keep my projects clean.
2. How to read HTML code and find specific "tags" and "classes."
3. How to use a `.gitignore` file so I don't upload junk files to GitHub. 
4. How to use `utf-8` encoding to prevent special characters from looking broken in the CSV.
5. How to mimic a real browser using User-Agents to avoid being blocked.
6. The difference between static and dynamic content.

## How to use it
1. Install the tools: `pip install requests beautifulsoup4`
2. Run the script: `quotes_scraper.py` or `jobs_scraper.py`
3. Check the CSV file for the results.

