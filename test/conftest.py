import pytest
from fixture.application import Application



fixture = None


@pytest.fixture
def app(request):
    global fixture
    # checking the fixture for validity
    if fixture is None:
        browser = request.config.getoption("--browser")
        fixture = Application(browser=browser)
        # login all tests
        fixture.session.login(user_name="admin", password="secret")
    else:
        if not fixture.is_valid():
            fixture = Application()
            fixture.session.login(user_name="admin", password="secret")
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
    parser.addoption("--browser", action="store", default="firefox")




