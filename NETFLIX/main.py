def main(url, module_name):
    import cloudscraper
    import json
    import os
    import requests

    scraper = cloudscraper.create_scraper()

    try:
        with open("./NETFLIX/query.json", "r") as query_file:
            query = json.load(query_file)
        with open("./NETFLIX/variables.json", "r") as var_file:
            variables = json.load(var_file)
        with open("./NETFLIX/cookies.json", "r") as var_file:
            cookies = json.load(var_file)
        payload = {
            "operationName":"DetailModal",
            "variables": variables,
            "extensions": {
                "persistedQuery":query
                }
        }
        data = scraper.post(url=url,json=payload,cookies=cookies)
        if data.status_code == 200:
            data = data.json()
        else:
            raise requests.exceptions.HTTPError(f"Failed to fetch data. HTTP Status Code: {data.status_code}")
        os.makedirs(os.path.join(os.getcwd(), 'result'), exist_ok=True)
        result_path = os.path.join(os.getcwd(), 'result', f'NETFLIX_{module_name}.json')
        with open(result_path, 'w') as f:
            json.dump(data, f, indent=4)
        print(f'{module_name} data saved to {result_path}')
    except OSError as e:
        print(f"File operation error while saving {module_name} data to {result_path}: {e}")
    except (TypeError, ValueError) as e:
        print(f"JSON processing error while saving {module_name} data: {e}")

url = {
    "movie": "https://web.prod.cloud.netflix.com/graphql",
}

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--module', choices=list(url.keys()), required=True)
    args = parser.parse_args()
    main(url[args.module], args.module)     