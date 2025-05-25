def transform(response):
    """Extracts the 'itemList' from a TikTok API response.

    Parses the JSON response and returns the list of items contained in the 'itemList' field.

    Args:
        response: The HTTP response object from the TikTok API.

    Returns:
        list: The list of items from the response.
    """
    return response.json()['itemList']