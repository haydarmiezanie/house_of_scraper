def main(url, module_name):
    import cloudscraper
    import json
    import os

    scraper = cloudscraper.create_scraper(
        browser={
            'browser' : 'chrome',
            'platform': 'windows',
            'desktop' : True
        }
    )
    
    try:
        data = scraper.get(url)
        if data.status_code == 200:
            data = json.loads(data.text)
        else:
            raise Exception(f"Failed to fetch data. HTTP Status Code: {data.status_code}")
        os.makedirs(os.path.join(os.getcwd(), 'result'), exist_ok=True)
        result_path = os.path.join(os.getcwd(), 'result', f'IDX_{module_name}.json')
        with open(result_path, 'w') as f:
            json.dump(data, f, indent=4)
        print(f'{module_name} data saved to {result_path}')
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

url ={
    'broker': 'https://www.idx.co.id/primary/TradingSummary/GetBrokerSummary?length=9999&start=0',
    'stocks': 'https://www.idx.co.id/primary/TradingSummary/GetStockSummary?length=9999&start=0',
    'index' : 'https://www.idx.co.id/primary/TradingSummary/GetIndexSummary?length=9999&start=0'
}

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--module', choices=list(url.keys()), required=True)
    args = parser.parse_args()
    main(url[args.module], args.module) 