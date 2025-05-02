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

    # Additional validation (only reached if subprocess succeeds)
    # Filter out benign warnings from stderr output. Adjust allowed_warning_substrings as needed.
    allowed_warning_substrings = ["Warning: Deprecated", "BenignWarningMessage"]
    unexpected_stderr = "\n".join(
        line
        for line in result.stderr.splitlines()
        if all(allowed not in line for allowed in allowed_warning_substrings)
    )
    assert not unexpected_stderr, f"Module {module_name} produced unexpected stderr output: {unexpected_stderr}"


def test_scraper_main_function(module_name):
    data = main(["--module", module_name])
    
    # Assertions
    assert data is not None, "Main function returned None"
    assert isinstance(data, (list, dict)), f"Expected list or dict, got {type(data).__name__}"