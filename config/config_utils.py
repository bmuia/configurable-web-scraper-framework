import yaml

def open_configuration_file(path="config/config.yaml"):
    """Load YAML config and return as dict."""
    with open(path, "r") as file:
        configuration = yaml.safe_load(file)
    return configuration
