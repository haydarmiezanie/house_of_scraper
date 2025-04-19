from helpers.load_config import load_config

def load_optional(config, flag, filepath):
    return load_config(filepath) if config.get(flag) else None