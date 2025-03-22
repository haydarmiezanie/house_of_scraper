def main(url, module_name):
    import cloudscraper
    import json
    import os
    import requests

    scraper = cloudscraper.create_scraper()

    try:
        if module_name == 'searchJobs':
            with open(f"./GLINTS/{module_name}.txt", "r") as query_file:
                query = query_file.read()
            with open("./GLINTS/variables.json", "r") as var_file:
                variables = json.load(var_file)
            payload = {
                "query": query,
                "variables": variables  # Ensure this is a dictionary
            }
            data = scraper.post(url=url,json=payload)
        else:
            data = scraper.get(url=url)
        if data.status_code == 200:
            data = data.json()
        else:
            raise requests.exceptions.HTTPError(f"Failed to fetch data. HTTP Status Code: {data.status_code}")
        os.makedirs(os.path.join(os.getcwd(), 'result'), exist_ok=True)
        result_path = os.path.join(os.getcwd(), 'result', f'GLINTS_{module_name}.json')
        with open(result_path, 'w') as f:
            json.dump(data, f, indent=4)
        print(f'{module_name} data saved to {result_path}')
    except OSError as e:
        print(f"File operation error while saving {module_name} data to {result_path}: {e}")
    except (TypeError, ValueError) as e:
        print(f"JSON processing error while saving {module_name} data: {e}")

url = {
    "searchJobs": "https://glints.com/api/v2/graphql?op=searchJobs",
    "companies": "https://glints.com/api/companies?limit=30&offset=0&includeHierarchicalLocation=true&attributes=[%22id%22,%22logo%22,%22name%22,%22updatedAt%22,%22IndustryId%22,%22CountryCode%22,%22CityId%22,%22LocationId%22]&include=[%7B%22association%22:%22Industry%22,%22attributes%22:[%22name%22]%7D,%7B%22association%22:%22Jobs%22,%22attributes%22:[%22id%22,%22status%22,%22isPublic%22,%22updatedAt%22]%7D,%7B%22association%22:%22City%22,%22attributes%22:[%22name%22]%7D,%7B%22association%22:%22Country%22,%22attributes%22:[%22name%22]%7D]&where=%7B%22status%22:%22VERIFIED%22,%22name%22:%7B%22not%22:null%7D%7D&order=magic"
}

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--module', choices=list(url.keys()), required=True)
    args = parser.parse_args()
    main(url[args.module], args.module)     