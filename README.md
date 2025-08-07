# 🏠 House of Scraper 🚀

**Your Swiss Army Knife for Web Scraping & Automation!**  

House of Scraper is a powerful Python-based toolkit designed to simplify web scraping, automation, and data extraction. Whether you're a developer, data scientist, or hobbyist, this repository provides ready-to-use scripts for scraping popular websites like **Netflix, Linkedin, Tiktok, and more!**  


## 🌟 Features  

✅ **Multi-Platform Support**: Scrape property listings, job postings, and product data from various websites.  
✅ **Easy-to-Use**: Pre-built scripts with clear instructions—just run and extract!  
✅ **Customizable**: Modify scripts to fit your specific scraping needs.  
✅ **Automation Ready**: Integrate with workflows for scheduled scraping.  
✅ **Data Export**: Save scraped data in semi structured formats (JSON).  

## ⚡ Quick Start  

### Prerequisites  
- Python 3.8+  
- Libraries: `requests`, `BeautifulSoup`, `pandas`, `cloudscraper`  

### Installation  
1. Clone the repo:  
   ```bash
   git clone https://github.com/haydarmiezanie/house_of_scraper.git
   cd house_of_scraper
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
3. Run a Scraper as code (example for tokopedia):
   ```bash
   py -m scraper --module "tokopedia.shop" --output json
   ```
   Use this mode when you want to run the scraper as a standalone script. It executes the full scraping process with default settings, which is ideal for quick execution or command line integration.
   
4. Run a scraper as function (example for tokopedia):
   ```bash
   py -m scraper --module "tokopedia.shop"
   ```
   Use this mode when you prefer to integrate the scraping functionality into your own Python code. It allows you to call the scraper as a function, offering better flexibility for customization within larger applications.
## 🛠 Customization
Each script is modular and adjustable:
- **Modify URLs**: Change the target website URL in the yaml.
- **Add Data Fields**: Extract additional data by editing the parsing logic.

[Example Custom](https://github.com/haydarmiezanie/house_of_scraper/blob/master/platform/linkedin.yaml)

## 📂 Data Output
Scraped data is saved in `/result` as:
- JSON (for APIs/databases)

[Example Output](https://github.com/haydarmiezanie/house_of_scraper/tree/master/result)

## 🤖 Ethical Scraping & Legal Note
**⚠ Use responsibly!**
- Respect robots.txt and website terms.
- Add delays (time.sleep()) to avoid overwhelming servers.

## 💬 Need Help?
Got questions or suggestions? Open an [**Issue**](https://github.com/haydarmiezanie/house_of_scraper/issues) or reach out:
- 📧 Email: haydarsaja@gmail.com
- 🐦 Linkedin: [Haydar Miezanie Abdul Jamil](https://www.linkedin.com/in/haydar-miezanie-abdul-jamil-916302162/)

## 📜 License
MIT © Haydar Miezanie Abdul Jamil – Free for personal and commercial use.

### How to Download This File:  
1. Copy the entire text above.  
2. Save it as `README.md` in your repository.  
3. Commit and push!  

Let me know if you'd like any modifications! 🎯
