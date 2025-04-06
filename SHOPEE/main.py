def main(url, module_name):
    import cloudscraper
    import json
    import os
    import requests
    from bs4 import BeautifulSoup

    scraper = cloudscraper.create_scraper(
        browser={
            'browser' : 'chrome',
            'platform': 'android',
            'desktop' : False
        }
    )

    try:
        data = scraper.get(url)
        if data.status_code != 200:
            raise requests.exceptions.HTTPError(f"Failed to fetch data. HTTP Status Code: {data.status_code}")
        soup = BeautifulSoup(data.text,'html.parser')
        script_tag = soup.find('script', {'type': 'text/mfe-initial-data'})
        data = json.loads(script_tag.text.strip())
        os.makedirs(os.path.join(os.getcwd(), 'result'), exist_ok=True)
        result_path = os.path.join(os.getcwd(), 'result', f'SHOPEE_{module_name}.json')
        with open(result_path, 'w') as f:
            json.dump(data, f, indent=4)
        print(f'{module_name} data saved to {result_path}')
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

url ={
    'product': 'https://shopee.co.id/product/318201981/11251238244',
    'shop': 'https://shopee.co.id/herbalstore_naturindo'
}

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--module', choices=list(url.keys()), required=True)
    args = parser.parse_args()
    main(url[args.module], args.module) 