def transform(response):
    """Extracts and returns the 'data' field from a JSON response object.

    This function assumes the response contains a JSON object with a 'data' key.

    Args:
        response: A response object with a .json() method.

    Returns:
        The value associated with the 'data' key in the JSON response.
    """
    return response.json()['data']