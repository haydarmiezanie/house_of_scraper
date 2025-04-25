def load_config(filepath):
    """Loads configuration data from a file.

    This function supports loading configuration data from JSON and YAML files. It raises an error if the file format is unsupported or if there's an issue loading the file.

    Args:
        filepath: The path to the configuration file.

    Returns:
        A dictionary containing the configuration data.

    Raises:
        RuntimeError: If the configuration file cannot be loaded due to an unsupported format, invalid data, or file not found error.
    """
    # Import necessary libraries
    import os,yaml,json
    
    # Check if the file exists
    _, ext = os.path.splitext(filepath.lower())

    # Check if the file has a supported extension
    try:
        # Check if the file exists
        with open(filepath, 'r') as f:
            # Load the file based on its extension
            if ext in ['.yaml', '.yml']:
                return yaml.safe_load(f)
            elif ext == '.json':
                return json.load(f)
            else:
                raise ValueError("Unsupported file format. Only .json and .yaml/.yml are supported.")
    except (yaml.YAMLError, json.JSONDecodeError, ValueError, FileNotFoundError) as e:
        raise RuntimeError(f"Error loading config file: {e}") from e