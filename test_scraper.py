import subprocess
import pytest
from scraper import main

# Test that the scraper modules can be imported and run without errors
# How to run this test:
# pytest test_scraper.py --module "module.sub_module" -v


def test_scraper_modules(module_name):
    try:
        result = subprocess.run(
            ['python', '-m', 'scraper', '--module', module_name],
            capture_output=True,
            text=True,
            check=True,  # Automatically raises CalledProcessError for non-zero return codes
            timeout=30,  # Add reasonable timeout to prevent hanging
        )
    except subprocess.TimeoutExpired as e:
        pytest.fail(f"Module {module_name} timed out after 30 seconds")
    except subprocess.CalledProcessError as e:
        pytest.fail(f"Module {module_name} failed with return code {e.returncode}: {e.stderr}")
    except Exception as e:
        pytest.fail(f"Unexpected error testing module {module_name}: {str(e)}")

    # Additional validation (only reached if subprocess succeeds)
    assert not result.stderr, f"Module {module_name} produced stderr output: {result.stderr}"

def test_scraper_main_function(module_name):
    data = main(["--module", module_name])
    
    # Assertions
    assert data is not None, "Main function returned None"
    assert isinstance(data, (list, dict)), f"Expected list or dict, got {type(data).__name__}"