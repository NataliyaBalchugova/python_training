import pytest
from fixture.application import Application

fixture = None


@pytest.fixture(scope="session")
def app(request):
    global fixture
    if fixture is None:
        fixture = Application()
        # login all tests
        fixture.session.login(user_name="admin", password="secret")
    else:
        if not fixture.is_valid():
            # fixture.destroy()
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
