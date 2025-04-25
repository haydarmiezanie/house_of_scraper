def transform(response):
    """Transforms a multi-line JSON response into a list of dictionaries.

    This function parses each line of the response text as a separate JSON object and returns them as a list.

    Args:
        response: The response object containing the multi-line JSON data.

    Returns:
        A list of dictionaries, where each dictionary represents a JSON object from a line in the response.
    """
    import json
    return [json.loads(line) for line in response.text.splitlines()]