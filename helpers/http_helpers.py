def make_request(scraper, request_type, url, headers, data, payload, cookies, timeout, transform_fn=None):
    try:
        if request_type == 'GET':
            response = scraper.get(url, headers=headers, cookies=cookies, timeout=timeout)
        else:
            response = scraper.post(url, headers=headers, data=data, json=payload, cookies=cookies, timeout=timeout)
        response.raise_for_status()
        return transform_fn(response) if transform_fn else response.json()
    except Exception as e:
        raise ValueError(f"Request failed: {str(e)}") from e