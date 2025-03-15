import argparse
import subprocess
import re

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--module', help='The Python module to run', required=True)
    args = parser.parse_args()
    module = args.module

    # Validate module name (allow dotted names but prevent injection)
    if not re.fullmatch(r'[a-zA-Z_][a-zA-Z0-9_]*(\.[a-zA-Z_][a-zA-Z0-9_]*)*', module):
        print("Error: Invalid module name format.")
    else:
        try:
            top_module = module.split('.')[0]
            sub_module = module.split('.')[1]
            subprocess.run(['python', '-m', f"{top_module}.main", "--module" , sub_module], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error executing module: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")