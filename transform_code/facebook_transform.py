def transform(response):
    import json
    return [json.loads(line) for line in response.text.splitlines()]