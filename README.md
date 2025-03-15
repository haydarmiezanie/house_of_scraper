# House of Scraper
### A Python-based tool for efficient web data extraction

## Overview
House of Scraper is a Python-based web scraping tool designed to extract data from various websites efficiently. Leveraging libraries such as `cloudscraper`, which helps bypass anti-bot measures and captchas, this tool simplifies the process of collecting and processing web data.
House of Scraper is a Python-based web scraping tool designed to extract data from various websites efficiently. Leveraging libraries such as `cloudscraper`, this tool simplifies the process of collecting and processing web data.

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
   Here, `"Folder.sub_folder"` represents the Python module path where your scraping logic is implemented. Replace `"Folder.sub_folder"` with the actual module path in your project. For example, if your scraper logic is in a file `stocks.py` inside a folder `IDX`, use `"IDX.stocks"`.

   Example:
   ```bash
   py -m scraper --module "IDX.stocks"
Check the result in : `/result` (this directory is automatically created by the tool if it does not already exist).
   py -m scraper --module "IDX.stocks"

## Any Issue ?

If you encounter any issues with the code, feel free to reach out:
- GitHub Issues: [Open an issue](https://github.com/haydarmiezanie/house_of_scraper/issues)
- Email: haydarsaja@gmail.com
- Linkedin: [Linkedin Contact](https://www.linkedin.com/in/haydar-miezanie-abdul-jamil-916302162/)