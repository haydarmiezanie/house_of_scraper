import argparse, json, yaml, os, importlib, re
from typing import Optional, List, Union, Dict, Any
from helpers.http_helpers import make_request
from helpers.load_optional import load_optional
from helpers.load_config import load_config
def create_scraper(library, options=None):
    libraries = {
        'cloudscraper': 'cloudscraper',
        'requests': 'requests'
    }

    if library not in libraries:
        raise ValueError(f"Unsupported library: {library}. Supported libraries are: {', '.join(libraries.keys())}.")

    try:
        module = importlib.import_module(libraries[library])
    except ImportError as e:
        raise ImportError(
            f"{libraries[library]} module is not installed. Please install it using 'pip install {libraries[library]}'."
        ) from e

    if library == 'cloudscraper':
        return module.create_scraper(**(options or {}))
    elif library == 'requests':
        return module.Session()

def get_nested_value(d, path):
    # Parse the path into components
    parts = re.findall(r'\[(.*?)\]', path)

    current = d
    for part in parts:
        # Handle both string keys and numeric indices
        if part.startswith('"') and part.endswith('"'):
            key = part[1:-1]  # Remove quotes
        else:
            try:
                key = int(part)  # Try to convert to integer
            except ValueError:
                key = part  # Fall back to string

        try:
            current = current[key]
        except (KeyError, IndexError) as e:
            raise KeyError(f"Key '{key}' not found in the nested structure.") from e

    return current

def generate_request(
    scraper,
    request_type: str,
    url: str,
    headers: Optional[dict] = None,
    data: Optional[dict] = None,
    result_transform: Optional[str] = None,
    payload: Optional[dict] = None,
    cookies: Optional[dict] = None,
    loop_scraper: bool = False,
    item_list: Optional[list] = None,
    additional_cleanup: Optional[str] = None,
    timeout: int = 10
) -> Union[List[Any], Dict[str, Any], Any]:
    """Generate and process HTTP requests with optional transformations.
    
    Args:
        scraper: HTTP client instance
        request_type: 'GET' or 'POST'
        url: Endpoint URL (may contain {url_id} placeholder)
        headers: Request headers
        data: Form data for POST
        result_transform: Module name for response transformation
        payload: JSON payload for POST
        cookies: Request cookies
        loop_scraper: Whether to process multiple items
        item_list: Items to process in loop mode
        additional_cleanup: Module name for ID cleanup
        timeout: Request timeout in seconds

    Returns:
        Processed response(s) as JSON or transformed data
    """
    request_type = request_type.upper()
    if request_type not in ('GET', 'POST'):
        raise ValueError("Request type must be 'GET' or 'POST'")

    # Pre-load transformation modules if specified
    transform_fn = None
    cleanup_fn = None

    if result_transform:
        try:
            module = importlib.import_module(f"transform_code.{result_transform}")
            transform_fn = module.transform
        except ImportError as e:
            raise ImportError(f"Failed to load transform module: {e}") from e

    if additional_cleanup:
        try:
            module = importlib.import_module(f"cleanup_code.{additional_cleanup}")
            cleanup_fn = module.cleanup
        except ImportError as e:
            raise ImportError(f"Failed to load cleanup module: {e}") from e

    if not loop_scraper:
        return make_request(scraper, request_type, url, headers, data, payload, cookies, timeout, transform_fn)
    if not item_list:
        raise ValueError("item_list required when loop_scraper=True")
    return [
        make_request(
            scraper,
            request_type,
            url.format(url_id=cleanup_fn(item) if cleanup_fn else item),
            headers,
            data,
            payload,
            cookies,
            timeout,
            transform_fn
        )
        for item in item_list
    ]

def save_result(
    data: Any,
    main_module: str,
    sub_module: str,
    result_dir: str = None,
    indent: int = None,
    verbose: bool = True
) -> str:
    """Save data to JSON file in organized directory structure.
    
    Args:
        data: Data to be serialized to JSON
        main_module: Primary module/category name
        sub_module: Secondary module/subcategory name
        result_dir: Custom output directory (defaults to './result')
        indent: JSON indentation (None for compact, int for pretty-print)
        verbose: Whether to print save confirmation
        
    Returns:
        Absolute path to the saved file
    """
    # Determine output directory
    base_dir = result_dir if result_dir is not None else os.path.join(os.getcwd(), 'result')

    # Ensure directory exists
    os.makedirs(base_dir, exist_ok=True)

    # Create safe filename
    filename = f"{main_module}_{sub_module}.json".replace(' ', '_').lower()
    filepath = os.path.join(base_dir, filename)

    # Atomic write operation
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=indent, ensure_ascii=False)
    except (IOError, TypeError) as e:
        raise RuntimeError(f"Failed to save data: {str(e)}") from e

    if verbose:
        print(f"Successfully saved {sub_module} data to {os.path.abspath(filepath)}")

    return filepath


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--module', help='The Python module to run', required=True)
    args = parser.parse_args()

    try:
        main_module, sub_module = args.module.split('.', 1)
    except ValueError as e:
        raise ValueError(
            "The '--module' argument must be in the format 'main.sub'"
        ) from e

    config = load_config(f"platform/{main_module}.yaml")
    module_config = config.get(main_module, {})
    sub_config = module_config.get(sub_module, {})

    scraper = create_scraper(
        library=module_config['library'],
        options=module_config.get('library_settings')
    )

    data = load_optional(sub_config,'insert_data', f"data/{main_module}_data.json")
    payload = load_optional(sub_config,'insert_payload', f"payload/{main_module}_payload.json")
    cookies = load_optional(sub_config,'insert_cookies', f"cookies/{main_module}_cookies.json")
    headers = load_optional(sub_config,'insert_headers', f"headers/{main_module}_headers.json")

    transform_value = sub_config.get('result_transform')
    transform = f"{main_module}_transform" if transform_value is True else transform_value

    additional_cleanup_value = sub_config.get('additional_cleanup')
    additional_cleanup = f"{main_module}_cleanup" if additional_cleanup_value is True else additional_cleanup_value

    if not sub_config.get('loop_scraper'):
        get_data = generate_request(
            scraper=scraper,
            request_type=sub_config['request_type'].upper(),
            url=sub_config['url'],
            data=data,
            result_transform=transform,
            payload=payload,
            headers=headers,
            cookies=cookies
        )
    else:
        main_list = load_config(f"result/{main_module}_{sub_config['main_list']}.json")
        list_url = get_nested_value(main_list, sub_config['cleanup_list'])

        get_data = generate_request(
            scraper=scraper,
            request_type=sub_config['request_type'].upper(),
            url=sub_config['url'],
            data=data,
            payload=payload,
            headers=headers,
            cookies=cookies,
            result_transform=transform,
            loop_scraper=True,
            item_list=list_url,
            additional_cleanup=additional_cleanup
        )

    save_result(data=get_data, main_module=main_module, sub_module=sub_module)

if __name__ == '__main__':
    main()


    
