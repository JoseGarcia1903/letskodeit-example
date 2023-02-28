import pytest
from base.webdriverfactory import WebDriverFactory

@pytest.fixture()
def setUp():
    print("Running Method SetUp")
    yield
    print("Running Method TearDown")


@pytest.fixture(scope="class")
def oneTimeSetUp(request, browser):
    print("Running One Time SetUp")
    wdb = WebDriverFactory(browser)
    driver = wdb.getDriverInstance()

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print("Running One Time TearDown")


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")
