import pytest
from fixture.application import Application
import json


fixture = None
target = None

@pytest.fixture
def app(request):
    global fixture
    global target
    browser = request.config.getoption("--browser")
    if target is None:
        with open(request.config.getoption("--target")) as config_file:
         target = json.load(config_file)
    # checking the fixture for validity
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=target["baseUrl"])
        # login all tests
    fixture.session.login(user_name=target["username"], password=target["password"])
    # fixture.session.login(user_name="admin", password="secret")
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    # logout all tests
    def fin():
        global fixture
        if fixture is not None:
            fixture.destroy()

    request.addfinalizer(fin)


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--target", action="store", default="target.json")




