import json

def main(url, module_name):
    import cloudscraper
    import os
    import requests

    scraper = cloudscraper.create_scraper()

    try:
        with open("./TIKTOK/headers.json", "r") as var_file:
            headers = json.load(var_file)
        data = scraper.get(url=url,headers=headers)
        if data.status_code == 200:
            data = data.json()
        else:
            raise requests.exceptions.HTTPError(f"Failed to fetch data. HTTP Status Code: {data.status_code}")
        os.makedirs(os.path.join(os.getcwd(), 'result'), exist_ok=True)
        result_path = os.path.join(os.getcwd(), 'result', f'TIKTOK_{module_name}.json')
        with open(result_path, 'w') as f:
            json.dump(data, f, indent=4)
        print(f'{module_name} data saved to {result_path}')
    except OSError as e:
        print(f"File operation error while saving {module_name} data to {result_path}: {e}")
    except (TypeError, ValueError) as e:
        print(f"JSON processing error while saving {module_name} data: {e}")

with open("./TIKTOK/token.json", "r") as token:
    token = json.load(token)

main_url = (
   f"&msToken={token['msToken']}",
   f"&X-Bogus={token['X-Bogus']}",
   f"&_signature={token['_signature']}",
)

url = {
    "reccomendation": ''.join(("https://www.tiktok.com/api/recommend/item_list/?WebIdLastTime=1744336256&aid=1988&app_language=id-ID&app_name=tiktok_web&browser_language=en-US&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F135.0.0.0%20Safari%2F537.36&channel=tiktok_web&clientABVersions=70508271%2C72437276%2C73184476%2C73343441%2C73356774%2C73411238%2C73439740%2C73464036%2C73518011%2C73521361%2C73526774%2C73542497%2C73556822%2C73560061%2C73560277%2C73560978%2C73563784%2C73568203%2C73569235%2C73569256%2C73570121%2C73590517%2C73598637%2C73608968%2C73610557%2C73624992%2C73635175%2C73639823%2C73641235%2C73647958%2C73661072%2C73661249%2C73662753%2C73686098%2C73692431%2C70138197%2C70156809%2C70405643%2C71057832%2C71200802%2C71381811%2C71516509%2C71803300%2C71962127%2C72360691%2C72408100%2C72854054%2C72892778%2C73004916%2C73171280%2C73208420%2C73385640%2C73574728%2C73628214&cookie_enabled=true&count=9&coverFormat=2&data_collection_enabled=true&device_id=7491867128036509192&device_platform=web_pc&device_type=web_h264&enable_cache=false&focus_state=true&from_page=fyp&history_len=5&isNonPersonalized=false&is_fullscreen=false&is_page_visible=true&itemID=&language=id&odinId=7491866847777604626&os=windows&priority_region=&pullType=1&referer=https%3A%2F%2Fwww.tiktok.com%2Fid-ID%2F&region=ID&root_referer=https%3A%2F%2Fwww.google.com%2F&screen_height=768&screen_width=1366&showAboutThisAd=true&showAds=true&tz_name=Asia%2FJakarta&verifyFp=verify_m9c4rxgv_njsD75YO_MHeK_4axr_8HRT_qYylgCgghJ2K&vv_count_fyp=2&watchLiveLastTime=&webcast_language=id-ID",)+main_url),
    "user": ''.join(("https://www.tiktok.com/api/discover/user/?WebIdLastTime=1744336256&aid=1988&app_language=id-ID&app_name=tiktok_web&browser_language=en-US&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F135.0.0.0%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&count=20&data_collection_enabled=true&device_id=7491867128036509192&device_platform=web_pc&discoverType=0&focus_state=true&from_page=following&history_len=11&is_fullscreen=false&is_page_visible=true&keyWord=&language=id-ID&needItemList=true&odinId=7491866847777604626&offset=0&os=windows&priority_region=&referer=&region=ID&screen_height=768&screen_width=1366&tz_name=Asia%2FJakarta&useRecommend=false&user_is_login=true&verifyFp=verify_m9c4rxgv_njsD75YO_MHeK_4axr_8HRT_qYylgCgghJ2K&webcast_language=id-ID",)+main_url),
    }

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--module', choices=list(url.keys()), required=True)
    args = parser.parse_args()
    main(url[args.module], args.module)     