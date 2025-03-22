def main(url, module_name):
    import cloudscraper
    import json
    import os
    import requests

    scraper = cloudscraper.create_scraper()

    try:
        with open(f"./TOKOPEDIA/{module_name}.txt", "r") as query_file:
            query = query_file.read()
        with open("./TOKOPEDIA/variables.json", "r") as var_file:
            variables = json.load(var_file)[module_name]
        with open("./TOKOPEDIA/headers.json", "r") as var_file:
            headers = json.load(var_file)
        payload = {
            "operationName":url.split('/')[-1],
            "query": query,
            "variables": variables  # Ensure this is a dictionary
        }
        data = scraper.post(url=url,json=payload,headers=headers)
        if data.status_code == 200:
            data = data.json()
        else:
            raise requests.exceptions.HTTPError(f"Failed to fetch data. HTTP Status Code: {data.status_code}")
        os.makedirs(os.path.join(os.getcwd(), 'result'), exist_ok=True)
        result_path = os.path.join(os.getcwd(), 'result', f'TOKOPEDIA_{module_name}.json')
        with open(result_path, 'w') as f:
            json.dump(data, f, indent=4)
        print(f'{module_name} data saved to {result_path}')
    except OSError as e:
        print(f"File operation error while saving {module_name} data to {result_path}: {e}")
    except (TypeError, ValueError) as e:
        print(f"JSON processing error while saving {module_name} data: {e}")

url = {
    "product": "https://gql.tokopedia.com/graphql/PDPGetLayoutQuery",
    "shop": "https://gql.tokopedia.com/graphql/ShopPageGetHeaderLayout"
}

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--module', choices=list(url.keys()), required=True)
    args = parser.parse_args()
    main(url[args.module], args.module)     