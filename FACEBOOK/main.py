def main(url, module_name):
    import json
    import os
    import requests

    try:
        with open("./FACEBOOK/data.json", "r") as pyld:
            pyld = json.load(pyld)
        payload = {
                "__a": "1",
                "__comet_req": "15",
                "fb_dtsg": "YOUR PAYLOAD",
                "variables": pyld['variables'],
                "doc_id": pyld['doc_id'],
            }
        data = requests.post(url=url,data=payload)
        if data.status_code == 200:
            json_array = [json.loads(line) for line in data.text.splitlines()]
        else:
            raise requests.exceptions.HTTPError(f"Failed to fetch data. HTTP Status Code: {data.status_code}")
        os.makedirs(os.path.join(os.getcwd(), 'result'), exist_ok=True)
        result_path = os.path.join(os.getcwd(), 'result', f'FACEBOOK_{module_name}.json')
        with open(result_path, 'w') as f:
            json.dump(json_array, f, indent=4)
        print(f'{module_name} data saved to {result_path}')
    except OSError as e:
        print(f"File operation error while saving {module_name} data to {result_path}: {e}")
    except (TypeError, ValueError) as e:
        print(f"JSON processing error while saving {module_name} data: {e}")



url = {
    "profile": "https://www.facebook.com/api/graphql/",
    "media": "https://www.facebook.com/api/graphql/",
    "story": "https://www.facebook.com/api/graphql/",
}

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--module', choices=list(url.keys()), required=True)
    args = parser.parse_args()
    main(url[args.module], args.module)     
