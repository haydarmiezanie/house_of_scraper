import subprocess
import pytest
from scraper import main

def test_scraper_modules(module_name):
    """Test that each scraper module runs without errors via subprocess."""
    result = subprocess.run(
        ['py', '-m', 'scraper', '--module', module_name],
        capture_output=True,
        text=True
    )
    
    assert result.returncode == 0, f"Module {module_name} failed with error: {result.stderr}"
    assert not result.stderr, f"Module {module_name} produced stderr output: {result.stderr}"

def test_scraper_main_function(module_name):
    """Test the scraper's main function directly."""
    try:
        data = main(["--module", module_name])
        print(f"Data returned from {module_name}: {data}")
        
        # Add assertions based on what you expect the output to be
        assert data is not None, "Main function returned None"
        assert isinstance(data, (list, dict)), "Expected data to be a list or dict"
        

        
    except Exception as e:
        pytest.fail(f"main() failed with exception: {str(e)}")