def cleanup(item_id):
    """Extract numerical ID from a string.

    This function uses a regular expression to find the first numerical sequence
    within the input string and returns it as a string.

    Args:
        item_id: The input string potentially containing a numerical ID.

    Returns:
        The extracted numerical ID as a string, or None if no numerical sequence is found.
    """
    import re
    return re.search(r"\d+", item_id).group()