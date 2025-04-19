# House of Scraper
### A Python-based tool for efficient web data extraction

## Overview
House of Scraper is a Python-based web scraping tool designed to extract data from various websites efficiently. Leveraging libraries such as `cloudscraper`, `beautifulsoup` and `requests`, which helps bypass anti-bot measures and captchas, this tool simplifies the process of collecting and processing web data.

## Features

- **Flexible Targeting**: Customize the scraper to extract specific elements from web pages.
- **JSON Export**: Save scraped data into JSON files for easy analysis and integration.
- **Error Handling**: Robust mechanisms to handle exceptions and ensure continuous operation.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/haydarmiezanie/house_of_scraper.git
2. **Install Package**:
   ```bash
   pip install -r requirements.txt
3. **Running Code**:
   ```bash
   py -m scraper --module "Folder.sub_folder"
   ```
   The `--module` argument specifies the Python module path where your scraping logic is implemented. This is necessary for the tool to locate and execute the scraping code. Replace `"Folder.sub_folder"` with the actual module path in your project.
   Example:
   ```bash
   py -m scraper --module "IDX.stocks"
   ```
Check the result in: `/result` (this directory is automatically created by the tool if it does not already exist).

   ## 🔧 How to Provide Headers, Cookies, and Payloads

You can customize the request details for your scraper by modifying the `scraper_config` dictionary.

```python
scraper_config = {
    "headers": {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json"
    },
    "cookies": {
        "sessionid": "your-session-id"
    },
    "payload": {
        "search": "house",
        "location": "New York"
    }
}

scraper = SomeWebsiteScraper(config=scraper_config)
scraper.run()


---

## ✅ **2. How to Use the Scraper**

Create a "Quick Start" section with a sample script or command-line usage:

### ✨ Suggested README Section:
```markdown
## 🚀 Quick Start Guide

### Step 1: Clone and Install
```bash
git clone https://github.com/haydarmiezanie/house_of_scraper.git
cd house_of_scraper
pip install -r requirements.txt


---

## ✅ **3. Fix Typos and Rename Folder**
You mentioned a folder named `platform` that should likely be renamed to `module` or `scrapers`.

Here’s how to do that:
1. **Rename the folder** (locally):
   ```bash
   mv house_of_scraper/platform house_of_scraper/scrapers


## Any Issue ?

If you encounter any issues with the code, feel free to reach out:
- GitHub Issues: [Open an issue](https://github.com/haydarmiezanie/house_of_scraper/issues)
- LinkedIn: [Haydar Miezanie](https://www.linkedin.com/in/haydar-miezanie-abdul-jamil-916302162/)
