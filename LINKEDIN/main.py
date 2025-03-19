def request(url):
    import requests
    import json

    # Define session
    session = requests.Session()

    # Your LinkedIn cookies (replace with actual values)
    with open('./LINKEDIN/cookies.json', 'r') as f:
        cookies = json.load(f)

    # Extract CSRF token from JSESSIONID
    csrf_token = cookies["JSESSIONID"].strip('"')

    # Define headers
    headers = {
        "csrf-token": csrf_token,
        "x-restli-protocol-version": "2.0.0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Accept": "application/json"
    }

    try:
        data = session.get(url,headers=headers, cookies=cookies)

        if data.status_code != 200:
            raise requests.exceptions.HTTPError(f"Failed to fetch data. HTTP Status Code: {data.status_code}")
        data = data.json()
        return data
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main(url, module_name):
    import re
    import os
    import json
    response=request(url)
    list_job = response["metadata"]["jobCardPrefetchQueries"][0]["prefetchJobPostingCardUrns"]
    list_data = []
    if module_name != 'people':
        for job_id in list_job:
            url_id = re.search(r"\d+", job_id).group()
            sub_url = {
                "job":f"https://www.linkedin.com/voyager/api/jobs/jobPostings/{url_id}?decorationId=com.linkedin.voyager.deco.jobs.web.shared.WebFullJobPosting-65&topN=1&topNRequestedFlavors=List(TOP_APPLICANT,IN_NETWORK,COMPANY_RECRUIT,SCHOOL_RECRUIT,HIDDEN_GEM,ACTIVELY_HIRING_COMPANY)"
            }
            data=request(sub_url.get(module_name, "Invalid Key"))
            list_data.append(data)
            print(f'Success scrape Job: {url_id}')
            
    list_data=response if module_name == 'people' else list_data
    os.makedirs(os.path.join(os.getcwd(), 'result'), exist_ok=True)
    result_path = os.path.join(os.getcwd(), 'result', f'LINKEDIN_{module_name}.json')
    with open(result_path, 'w') as f:
        json.dump(list_data, f, indent=4)
    print(f'{module_name} data saved to {result_path}')

    
url = {
        'job': 'https://www.linkedin.com/voyager/api/voyagerJobsDashJobCards?decorationId=com.linkedin.voyager.dash.deco.jobs.search.JobSearchCardsCollection-218&count=25&q=jobSearch&query=(origin:JOB_COLLECTION_PAGE_SEARCH_BUTTON,locationUnion:(geoId:102478259),spellCorrectionEnabled:true)&start=0',
        'people': 'https://www.linkedin.com/voyager/api/graphql?includeWebMetadata=true&variables=(start:0,origin:SWITCH_SEARCH_VERTICAL,query:(flagshipSearchIntent:SEARCH_SRP,queryParameters:List((key:resultType,value:List(PEOPLE))),includeFiltersInResponse:false))&queryId=voyagerSearchDashClusters.9c3177ca40ed191b452e1074f52445a8'
    }

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--module', choices=list(url.keys()), required=True)
    args = parser.parse_args()
    main(url[args.module], args.module) 
