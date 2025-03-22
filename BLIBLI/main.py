def main(url, module_name):
    import cloudscraper
    import json
    import os
    import requests
    
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
            raise requests.exceptions.HTTPError(f"Failed to fetch data. HTTP Status Code: {data.status_code}")
        os.makedirs(os.path.join(os.getcwd(), 'result'), exist_ok=True)
        result_path = os.path.join(os.getcwd(), 'result', f'BLIBLI_{module_name}.json')
        with open(result_path, 'w') as f:
            json.dump(data, f, indent=4)
        print(f'{module_name} data saved to {result_path}')
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

url ={
    'product': 'https://www.blibli.com/backend/product-detail/products/is--NAS-60241-00022-00001/_summary?pickupPointCode=PP-3538616&cnc=false&fetchAllAvailability=true',
    'shop': 'https://www.blibli.com/backend/search/merchant/NAS-60241?excludeProductList=true&promoTab=false&pickupPointCode=PP-3538616&multiCategory=true&merchantSearch=false&pickupPointLatLong=&defaultPickupPoint=true&showFacet=false'
}

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--module', choices=list(url.keys()), required=True)
    args = parser.parse_args()
    main(url[args.module], args.module) 