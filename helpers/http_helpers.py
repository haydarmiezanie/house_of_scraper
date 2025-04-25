def make_request(scraper, request_type, url, headers, data, payload, cookies, timeout, transform_fn=None):
    """Makes an HTTP request using the provided scraper.

    This function handles both GET and POST requests and raises an exception if the request fails.  It also allows for custom transformation of the response.

    Args:
        scraper: The scraper object to use for making the request.
        request_type: The type of request ('GET' or 'POST').
        url: The URL to make the request to.
        headers: The headers to include in the request.
        data: The data to send in the request body (for POST requests).
        payload: The JSON payload to send in the request body (for POST requests).
        cookies: The cookies to include in the request.
        timeout: The timeout for the request.
        transform_fn: An optional function to transform the response.

    Returns:
        The JSON response from the server, or the transformed response if transform_fn is provided.

    Raises:
        ValueError: If the request fails.
    """
    # Validate request type
    try:
        # Validate request type
        if request_type == 'GET':
            response = scraper.get(url, headers=headers, cookies=cookies, timeout=timeout)
        else:
            response = scraper.post(url, headers=headers, data=data, json=payload, cookies=cookies, timeout=timeout)
        response.raise_for_status()
        return transform_fn(response) if transform_fn else response.json()
    except Exception as e:
        raise ValueError(f"Request failed: {str(e)}") from e