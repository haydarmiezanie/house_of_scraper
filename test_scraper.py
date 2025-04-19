import subprocess
import pytest

# List of modules to test (same as your original list)
MODULES_TO_TEST = [
    #'blibli.shop', can only manually run this module
    #'facebook.media', Need fixing
    'glints.searchjob',
    'idx.stocks',
    'instagram.media',
    'linkedin.job',
    'netflix.movie',
    'shopee.shop',
    'tiktok.reccomendation',
    'tokopedia.shop',
    'x.lists'
]

@pytest.mark.parametrize("module_name", MODULES_TO_TEST)
def test_scraper_modules(module_name):
    """Test that each scraper module runs without errors."""
    result = subprocess.run(
        ['py', '-m', 'scraper', '--module', module_name],
        capture_output=True,
        text=True
    )
    
    # Assert that the process completed successfully (return code 0)
    assert result.returncode == 0, f"Module {module_name} failed with error: {result.stderr}"
    
    # You might want to add more specific assertions based on what your scraper outputs
    # For example, if it should always output some JSON data:
    # assert result.stdout.strip().startswith('{') or result.stdout.strip().startswith('[')
    
    # Or if it should never output to stderr:
    assert not result.stderr, f"Module {module_name} produced stderr output: {result.stderr}"

def test_all_modules_in_list():
    """Test that all expected modules are in the test list."""
    expected_modules = [
        #'blibli.shop',
        #'facebook.media',
        'glints.searchjob',
        'idx.stocks',
        'instagram.media',
        'linkedin.job',
        'netflix.movie',
        'shopee.shop',
        'tiktok.reccomendation',
        'tokopedia.shop',
        'x.lists'
    ]
    
    assert sorted(MODULES_TO_TEST) == sorted(expected_modules), \
        "Test list doesn't match expected modules"