import pytest
from fixture.application import Application



fixture = None


@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    base_url = request.config.getoption("--baseUrl")
    # checking the fixture for validity
    if fixture is None:
        fixture = Application(browser=browser, base_url=base_url)
        # login all tests
        fixture.session.login(user_name="admin", password="secret")
    else:
        if not fixture.is_valid():
            fixture = Application(browser=browser, base_url=base_url)
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
    parser.addoption("--baseUrl", action="store", default="http://localhost/addressbook/")




