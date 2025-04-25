from helpers.logger import setup_logger

logger = setup_logger(__name__)

def transform(response):
    """Extracts JSON data from a Shopee response.

    This function parses the HTML content of the response, locates a specific script tag containing JSON data, and returns the parsed JSON object.

    Args:
        response: The response object containing the HTML content.

    Returns:
        The parsed JSON object extracted from the script tag.

    Raises:
        ValueError: If no script tag with the specified type is found.
    """
    # Importing necessary libraries
    from bs4 import BeautifulSoup
    import json

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the script tag with the specified type
    script_tag = soup.find('script', {'type': 'text/mfe-initial-data'})
    
    # If the script tag is not found, raise a ValueError
    if script_tag is None:
        raise logger.error("No script tag found with type 'text/mfe-initial-data'")
    
    return json.loads(script_tag.text.strip())