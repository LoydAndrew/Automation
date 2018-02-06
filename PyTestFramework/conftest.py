import pytest

@pytest.yield_fixture()

def setUp():
    print ("Running  method level setUp")
    yield
    print("\nOnce yield method level TEARDOWN after every method")


@pytest.yield_fixture(scope="module")
def onetimesetUp(browser,os_type):
    print("Running onetimesetUp test")
    if browser == "Firefox":
        print ("Running on Firefox")
    else:
        print("Running on Chrome")
    yield
    print("\nOnce yield after all tests are done")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--os_type",help='operating system')

@pytest.fixture(scope="module")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="module")
def os_type(request):
    return request.config.getoption("--os_type")