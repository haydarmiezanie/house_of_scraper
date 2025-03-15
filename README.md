# House of Scraper
### A Python-based tool for efficient web data extraction

## Overview
House of Scraper is a Python-based web scraping tool designed to extract data from various websites efficiently. Leveraging libraries such as `cloudscraper`, which helps bypass anti-bot measures and captchas, this tool simplifies the process of collecting and processing web data.

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
   

## Any Issue ?

If you encounter any issues with the code, feel free to reach out:
- GitHub Issues: [Open an issue](https://github.com/haydarmiezanie/house_of_scraper/issues)
- LinkedIn: [Haydar Miezanie](https://www.linkedin.com/in/haydar-miezanie-abdul-jamil-916302162/)
test