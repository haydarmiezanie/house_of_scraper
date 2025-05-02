def pytest_addoption(parser):
    """Adds the '--module' command line option to pytest.

    This option allows the user to specify a list of module names to test,
    and can be used multiple times to add multiple modules.
    """
    ## Add a command line option to pytest to specify module names
    ## to test. The option can be used multiple times to specify multiple modules.
    parser.addoption(
        "--module", 
        action="append",
        default=[],
        help="list of module names to test (can be used multiple times)"
    )

def pytest_generate_tests(metafunc):
    import pytest
    """Generates tests for specified modules.

    If the 'module_name' fixture is used in a test function, this function
    retrieves the list of modules provided via the '--module' command line option
    and parameterizes the test function with each module name. If no modules are
    provided, the test is skipped.
    """
    ## Check if the 'module_name' fixture is in the test function's fixture names
    ## If it is, retrieve the list of modules from the command line options
    ## and parameterize the test function with each module name.
    if "module_name" in metafunc.fixturenames:
        modules = metafunc.config.getoption("module")
        if not modules:
            pytest.skip("No modules provided via --module argument")
        metafunc.parametrize("module_name", modules)
