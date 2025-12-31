# 🚀 Automated Remote Job Scraper
A robust Python-based web scraper designed to extract the latest Full-Stack Programming opportunities from We Work Remotely. This tool is fully automated to run daily, ensuring you never miss a new job posting.

## ✨ Features

* **Live Extraction**: Scrapes job titles, company names, and direct application links.<br>
* **Smart Parsing**: Uses BeautifulSoup to clean HTML and handle nested elements (like company icons).<br>
* **Automated Pipeline**: Integrated with Windows Task Scheduler to run daily at 9:00 AM.<br>
* **Resilient Code**: Includes custom HTTP headers (User-Agent) to mimic real browser behavior and avoid blocks.<br>

## 🛠️ Technical Stack
* **Language**: Python 3.x
* **Libraries**: `requests`, `BeautifulSoup4`, `csv`
* **Environment**: Virtual Environment (`venv`) for dependency management.

## 📋 Installation and Setup

1. Install the tools: `pip install requests beautifulsoup4`
2. Run the script: `jobs_scraper.py`
3. Check the CSV file for the results (See jobs_example.csv if curious)

## 🤖 Automation (Windows Task Scheduler)

To keep the job list fresh without manual intervention, I configured a daily automation.<br>
A batch file was created to trigger the specific Python interpreter within the virtual environment:<br>
`run_scraper.bat`

1. Task: Created a new task in Windows Task Scheduler.
2. Trigger: Set to run Daily at 9:00 AM.
3. Action: Executes run_scraper.bat.
4. Reliability: Configured the "Start In" directory to the project root to ensure the jobs.csv is updated correctly.


