def pytest_addoption(parser):
    parser.addoption(
        "--module", 
        action="append",
        default=[],
        help="list of module names to test (can be used multiple times)"
    )

def pytest_generate_tests(metafunc):
    if "module_name" in metafunc.fixturenames:
        modules = metafunc.config.getoption("module")
        if not modules:
            pytest.skip("No modules provided via --module argument")
        metafunc.parametrize("module_name", modules)
