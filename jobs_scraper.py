import requests
from bs4 import BeautifulSoup
import csv

def run_scraper():
    # URL for programming jobs
    url = "https://weworkremotely.com/categories/remote-full-stack-programming-jobs"

    # Adding a user-agent so the site thinks this is a real browser
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"}

    print(f"\nConnecting to {url}...")

    # Downloading the page
    response = requests.get(url, headers=headers)

    # Parsing the HTML
    soup = BeautifulSoup(response.text, "html.parser")
    # print(soup.prettify())
    # Finding the data
    jobs_data = []
    job_postings = soup.find_all("li", class_="new-listing-container")
    # On this site, each job is in a <li class= "new-listing-container">
    # 'job_postings' contains a list in which each element is the
    # code for a unique job posting


    for j in job_postings:
        title_tag = j.find("h3", class_="new-listing__header__title")
        company_tag = j.find("p", class_="new-listing__company-name")

        # Only proceed if above tags exist for the job title and company name
        if title_tag and company_tag:
            job_title = title_tag.text.strip()
            company = company_tag.get_text(strip=True)
        else:
            job_title = "N/A"
            company = "N/A"

        # Getting the link for the job posting
        link_tag = j.find("a", recursive=False)
        # Making the full URL
        job_url = f"https://weworkremotely.com{link_tag.get("href") if link_tag else 'N/A'}"

        # Organize data in dictionaries within the list: 'jobs_data'
        jobs_data.append({"Job Title": job_title, "Company": company, "Link": job_url})

    # Save data in CSV
    filename = "jobs.csv"
    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["Job Title", "Company", "Link"])
        writer.writeheader()
        writer.writerows(jobs_data)

    print(f"\nSuccess! Saved {len(jobs_data)} jobs to {filename}.")

if __name__ == "__main__":
    run_scraper()
