import cloudscraper
import json
import os
import requests

if __name__ == '__main__':
    scraper = cloudscraper.create_scraper(
        browser={
            'browser': 'chrome',
            'platform': 'windows',
            'desktop': True,
            'mobile': False
        }
    )
    
    url = 'https://www.idx.co.id/primary/TradingSummary/GetStockSummary?length=9999&start=0&date=20250303'
    try:
        data = scraper.get(url)
        if data.status_code == 200:
            data = json.loads(data.text)
        else:
            raise Exception(f"Failed to fetch data. HTTP Status Code: {data.status_code}")
        os.makedirs(os.path.join(os.getcwd(), 'result'), exist_ok=True)
        result_path = os.path.join(os.getcwd(), 'result', 'IDX_stocks.json')
        with open(result_path, 'w') as f:
            json.dump(data, f, indent=4)
        print(f'Stocks data saved to {result_path}')
    except Exception as e:
        print(f"An unexpected error occurred: {e}")    