def main(url, module_name):
    import cloudscraper
    import json
    import os
    import requests

    scraper = cloudscraper.create_scraper()

    try:
        with open("./INSTAGRAM/cookies.json", "r") as cookie:
            cookies = json.load(cookie)
        with open("./INSTAGRAM/headers.json", "r") as header:
            headers = json.load(header)
        data = scraper.get(url=url,headers=headers,cookies=cookies)
        if data.status_code == 200:
            data = data.json()
        else:
            raise requests.exceptions.HTTPError(f"Failed to fetch data. HTTP Status Code: {data.status_code}")
        os.makedirs(os.path.join(os.getcwd(), 'result'), exist_ok=True)
        result_path = os.path.join(os.getcwd(), 'result', f'INSTAGRAM_{module_name}.json')
        with open(result_path, 'w') as f:
            json.dump(data, f, indent=4)
        print(f'{module_name} data saved to {result_path}')
    except OSError as e:
        print(f"File operation error while saving {module_name} data to {result_path}: {e}")
    except (TypeError, ValueError) as e:
        print(f"JSON processing error while saving {module_name} data: {e}")

url = {
    "media": "https://www.instagram.com/api/v1/media/3607326182471703618/info/",
    "follower": "https://www.instagram.com/api/v1/friendships/5888663093/followers/?count=100",
    "following": "https://www.instagram.com/api/v1/friendships/1610653794/following/?count=100"
}

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--module', choices=list(url.keys()), required=True)
    args = parser.parse_args()
    main(url[args.module], args.module)     