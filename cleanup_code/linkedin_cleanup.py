def cleanup(item_id):
    import re
    return re.search(r"\d+", item_id).group()