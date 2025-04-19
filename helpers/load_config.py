import os,yaml,json
def load_config(filepath):
    _, ext = os.path.splitext(filepath.lower())

    try:
        with open(filepath, 'r') as f:
            if ext in ['.yaml', '.yml']:
                return yaml.safe_load(f)
            elif ext == '.json':
                return json.load(f)
            else:
                raise ValueError("Unsupported file format. Only .json and .yaml/.yml are supported.")
    except (yaml.YAMLError, json.JSONDecodeError, ValueError, FileNotFoundError) as e:
        raise RuntimeError(f"Error loading config file: {e}") from e