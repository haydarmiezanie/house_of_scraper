def load_optional(config, flag, filepath):
    """Conditionally loads a configuration file.

    This function checks if a flag is present in the config and if so, loads the file specified by filepath.  If the flag is not present, it returns None.

    Args:
        config (dict): The configuration dictionary.
        flag (str): The flag to check for in the config.
        filepath (str): The path to the file to load if the flag is present.

    Returns:
        dict or None: The loaded configuration data if the flag is present, otherwise None.
    """
    # Import the load_config function from the helpers module
    from helpers.load_config import load_config
    return load_config(filepath) if config.get(flag) else None