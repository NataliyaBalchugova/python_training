
import pytest
from fixture.application import Application

@pytest.fixture(scope = "session")
def app(request):
    fixture = Application()
    return fixture