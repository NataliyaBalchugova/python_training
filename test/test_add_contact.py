# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from fixture.application_for_contact import ApplicationContact

@pytest.fixture
def app(request):
    fixture = ApplicationContact()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    #wd = self.wd
    app.open_home_page()
    app.login(username="admin", password="secret")
    app.fill_contact(Contact(firstname="Alexandr", lastname="Ponomarev", work="System Administrator",
                                      address="Demakova, 5"))
    app.logout()

