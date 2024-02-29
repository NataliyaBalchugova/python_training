import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    return fixture


def test_add_contact(app):
    app.session.login(user_name="admin", password="secret")
    app.contact.fill_contact(Contact(firstname="Alexandr", lastname="Ponomarev", work="System Administrator",
                                      address="Demakova, 5"))
    app.session.logout()