from typing import Optional, List, Union, Dict, Any
from helpers.logger import setup_logger
from helpers.regex_helpers import get_first_level
logger = setup_logger(__name__)
def create_scraper(library, options=None):
    """Creates a web scraper instance based on the specified library.

    This function supports creating scrapers using either 'cloudscraper' or 'requests'. It handles importing the necessary library and creating the scraper instance with provided options.

    Args:
        library: The name of the scraping library ('cloudscraper' or 'requests').
        options: Optional dictionary of settings to pass to the scraper's constructor.

    Returns:
        A scraper instance (either a cloudscraper object or a requests.Session object).

    Raises:
        ValueError: If the specified library is not supported.
        ImportError: If the specified library is not installed.
    """
    # Define supported libraries and their import paths
    import importlib

    # Define the mapping of library names to their import paths
    libraries = {
        'cloudscraper': 'cloudscraper',
        'requests': 'requests'
    }

    # Check if the specified library is supported
    if library not in libraries:
        raise ValueError(f"Unsupported library: {library}. Supported libraries are: {', '.join(libraries.keys())}.")

    # Attempt to import the specified library
    try:
        module = importlib.import_module(libraries[library])
    except ImportError as e:
        raise logger.error(
            f"{libraries[library]} module is not installed. Please install it using 'pip install {libraries[library]}'."
        ) from e

    # Create the scraper instance based on the specified library
    if library == 'cloudscraper':
        return module.create_scraper(**(options or {}))
    elif library == 'requests':
        return module.Session()

def _traverse_path(d: Any, path: str) -> Any:
    """Retrieves a value from a nested dictionary or list using a string path.

    This function supports both string and integer keys, and raises an error if a key or index is not found.

    Args:
        d (Any): The dictionary or list to traverse.
        path (str): The string path representing the nested keys and/or indices.

    Returns:
        Any: The value found at the specified path.

    Raises:
        KeyError: If a key or index is not found in the nested structure.
    """
    import re
    parts = re.findall(r'\[(.*?)\]', path)
    current = d
    for part in parts:
        if part.startswith('"') and part.endswith('"'):
            key = part[1:-1]
        else:
            try:
                key = int(part)
            except ValueError:
                key = part
        try:
            current = current[key]
        except (KeyError, IndexError) as e:
            logger.error(f"Key '{key}' not found in the nested structure.")
            raise KeyError(key) from e
    return current

def get_nested_value(d, path):
    """Retrieves a value or list of values from a nested dictionary or list using a string path.

    Supports indexed access for lists when '{}' is present in the path, otherwise returns a single value.

    Args:
        d: The dictionary or list to traverse.
        path: The string path representing the nested keys and/or indices.

    Returns:
        Any: The value(s) found at the specified path.
    """
    if '{}' in path:
        count = len(get_first_level(d, path))
        return [_traverse_path(d, path.format(i)) for i in range(count)]
    return _traverse_path(d, path)

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
    subitem_list: Optional[list] = None,
    additional_cleanup: Optional[str] = None,
    timeout: int = 10
    ) -> Union[List[Any], Dict[str, Any], Any]:
    """Generates and executes HTTP requests using the provided scraper and parameters.

    Supports single or looped requests, optional result transformation, and additional cleanup logic.

    Args:
        scraper: The scraper instance to use for making requests.
        request_type (str): The HTTP request type ('GET' or 'POST').
        url (str): The URL or URL template for the request(s).
        headers (Optional[dict]): Optional HTTP headers to include.
        data (Optional[dict]): Optional data to send in the request.
        result_transform (Optional[str]): Optional name of a result transformation module.
        payload (Optional[dict]): Optional payload to send in the request.
        cookies (Optional[dict]): Optional cookies to include in the request.
        loop_scraper (bool): Whether to loop over a list of items to make multiple requests.
        item_list (Optional[list]): List of items to use in URL formatting if looping.
        subitem_list (Optional[list]): Optional list of subitems for additional URL formatting.
        additional_cleanup (Optional[str]): Optional name of a cleanup module to apply to items.
        timeout (int): Timeout for the request(s) in seconds.

    Returns:
        Union[List[Any], Dict[str, Any], Any]: The result(s) of the HTTP request(s).

    Raises:
        Warning: If the request type is not 'GET' or 'POST', or if item_list is missing when loop_scraper is True.
        ImportError: If the specified transform or cleanup module cannot be loaded.
    """
    import importlib
    from helpers.http_helpers import make_request
    from itertools import zip_longest 

    # Validate request type
    request_type = request_type.upper()
    if request_type not in ('GET', 'POST'):
        raise logger.warning("Request type must be 'GET' or 'POST'")

    # Pre-load transformation modules if specified
    transform_fn = None
    cleanup_fn = None

    # Check if result_transform is provided and import the module
    if result_transform:
        try:
            module = importlib.import_module(f"transform_code.{result_transform}")
            transform_fn = module.transform
        except ImportError as e:
            raise logger.error(f"Failed to load transform module: {e}") from e

    # Check if additional_cleanup is provided and import the module
    if additional_cleanup:
        try:
            module = importlib.import_module(f"cleanup_code.{additional_cleanup}")
            cleanup_fn = module.cleanup
        except ImportError as e:
            raise logger.error(f"Failed to load cleanup module: {e}") from e

    # If loop_scraper is enabled, ensure item_list is provided
    if not loop_scraper:
        return make_request(scraper, request_type, url, headers, data, payload, cookies, timeout, transform_fn)
    if not item_list:
        raise logger.warning("item_list required when loop_scraper=True")
    fmt_id = cleanup_fn or (lambda x: x)

    return [
        make_request(
            scraper,
            request_type,
            url.format(
                url_id=fmt_id(item),
                **(
                    {"additional_url": fmt_id(subitem)}
                    if subitem_list and subitem is not None
                    else {}
                )
            ),
            headers, data, payload, cookies,
            timeout,
            transform_fn
        )
        for item, subitem in zip(item_list, subitem_list or [None]*len(item_list))
    ]

def save_result(
    data: Any,
    main_module: str,
    sub_module: str,
    output: str,
    result_dir: str = None,
    indent: int = None
    ) -> str:
    """Saves the provided data to a file in the specified format.

    This function supports saving data as JSON, CSV, Parquet, or to a DuckDB database. It creates the output directory if it does not exist and returns the path to the saved file.

    Args:
        data: The data to be saved.
        main_module: The main module name, used in the filename.
        sub_module: The submodule name, used in the filename.
        output: The output format ('json', 'csv', 'parquet', or 'db').
        result_dir: Optional directory to save the result.
        indent: Indentation level for JSON output.
        verbose: Whether to log a success message.

    Returns:
        The absolute path to the saved file.

    Raises:
        IOError: If there is an error writing the file.
        TypeError: If the data is not serializable in the chosen format.
    """
    import json, os, csv
    import pandas as pd

    if output not in ['json', 'csv', 'parquet', 'db']:
        raise logger.error(f"Unsupported output: {output}")
    # Determine output directory
    base_dir =  os.path.join(result_dir, output) if result_dir is not None else os.path.join(os.getcwd(), 'result', output)

    # Ensure directory exists
    os.makedirs(base_dir, exist_ok=True)

    # Create safe filename
    filename = f"{main_module}_{sub_module}.{output}".replace(' ', '_').lower() if output != 'db' else f"{main_module}.{output}".replace(' ', '_').lower()
    filepath = os.path.join(base_dir, filename)

    # Atomic write operation
    try:
        if output == 'json':
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=indent, ensure_ascii=False)
        elif output == 'csv':
            # Validate and normalize data
            if isinstance(data, list):
                if not data:
                    raise logger.error("Cannot write CSV: data list is empty")
                rows = data
            elif isinstance(data, dict):
                rows = [data]
            else:
                raise logger.error("Cannot write CSV: data must be a dict or list of dicts")
            fieldnames = set()
            for row in data:
                fieldnames.update(row.keys())
            with open(filepath, 'w', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(rows)
        elif output=='parquet':
            df = pd.DataFrame(data if type(data) is list else [data])
            df.to_parquet(filepath, index=False)
        elif output=='db':
            import duckdb
            df = pd.DataFrame(data if type(data) is list else [data])
            conn = duckdb.connect(database=filepath)

            # Register the DataFrames as temporary views
            conn.register(f"{main_module}_{sub_module}", df)

            # Create tables from the DataFrames
            conn.execute(f"CREATE OR REPLACE TABLE {main_module}.{sub_module} AS SELECT * FROM df")

            # Optional: Unregister the temporary views
            conn.unregister(f"{main_module}_{sub_module}")

            # Verify and close
            conn.close()
    except (IOError, TypeError) as e:
        raise logger.error(f"Failed to save data: {str(e)}") from e

    logger.info(f"Successfully saved {sub_module} data to {os.path.abspath(filepath)}")

    return filepath


def main(args: Optional[List[str]] = None)-> Dict[str, Any]:
    """Executes the scraping process based on command-line arguments.

    Loads configuration, creates a scraper, makes requests, transforms results,
    and saves or returns the data.
    Args:
        args: Optional list of command-line arguments.

    Returns:
        A dictionary containing the scraped data if no output file is specified.

    Raises:
        ValueError: If the '--module' argument is not in the correct format.
        ImportError: If the specified transform or cleanup module cannot be loaded.
    """
    # Import necessary modules
    import argparse
    from helpers.load_optional import load_optional
    from helpers.load_config import load_config

    # Parse command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--module', help='The Python module to run', required=True)
    parser.add_argument("--output", help="Output file (default: print to stdout)")
    args = parser.parse_args(args=args)

    # Validate module argument
    try:
        main_module, sub_module = args.module.split('.', 1)
    except ValueError as e:
        raise logger.error(
            "The '--module' argument must be in the format 'main.sub'"
        ) from e

    # Load configuration
    config = load_config(f"platform/{main_module}.yaml")
    module_config = config.get(main_module, {})
    sub_config = module_config.get(sub_module, {})
    if not sub_config or not module_config:
        raise logger.error(f"The module does not exist. Please check the configuration: /platfomrm/{main_module}.json")

    # Check if the module is enabled
    scraper = create_scraper(
        library=module_config['library'],
        options=module_config.get('library_settings')
    )

    # Check if the module is enabled
    data = load_optional(sub_config,'insert_data', f"data/{main_module}_data.json")
    payload = load_optional(sub_config,'insert_payload', f"payload/{main_module}_payload.json")   
    cookies = load_optional(sub_config,'insert_cookies', f"cookies/{main_module}_cookies.json")
    if cookies is not None and "FIND THIS ITEM IN COOKIES" in cookies.values():
        raise logger.error(f"The cookies is not configure correctly. Please check the configuration: /cookies/{main_module}_cookies.json")
    headers = load_optional(sub_config,'insert_headers', f"headers/{main_module}_headers.json")
    if headers is not None and "FIND THIS ITEM IN HEADERS" in headers.values():
        raise logger.error(f"The headers is not configure correctly. Please check the configuration: /headers/{main_module}_headers.json")
    transform_value = sub_config.get('result_transform')
    transform = f"{main_module}_transform" if transform_value is True else transform_value
    additional_cleanup_value = sub_config.get('additional_cleanup')
    additional_cleanup = f"{main_module}_cleanup" if additional_cleanup_value is True else additional_cleanup_value
    subcleanup_list = sub_config.get('subcleanup_list',None)
    
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
        main_list = load_config(f"result/json/{main_module}_{sub_config['main_list']}.json")
        list_url = get_nested_value(main_list, sub_config['cleanup_list'])
        if subcleanup_list is not None:
           subcleanup_list = get_nested_value(main_list, sub_config['subcleanup_list'])
        get_data = generate_request(
            scraper=scraper,
            request_type=sub_config['request_type'].upper(),
            url=sub_config['url'],
            subitem_list=subcleanup_list,
            data=data,
            payload=payload,
            headers=headers,
            cookies=cookies,
            result_transform=transform,
            loop_scraper=True,
            item_list=list_url,
            additional_cleanup=additional_cleanup
        )

    # Check if output is not parsing then return dictionary
    if args.output is not None:
        save_result(data=get_data, 
                    main_module=main_module, 
                    sub_module=sub_module, 
                    output=args.output,
                    indent=4)
    else:
        return get_data

if __name__ == '__main__':
    main()


    
