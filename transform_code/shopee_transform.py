def transform(response):
    from bs4 import BeautifulSoup
    import json
    soup = BeautifulSoup(response.text, 'html.parser')
    script_tag = soup.find('script', {'type': 'text/mfe-initial-data'})
    
    if script_tag is None:
        raise ValueError("No script tag found with type 'text/mfe-initial-data'")
    
    return json.loads(script_tag.text.strip())