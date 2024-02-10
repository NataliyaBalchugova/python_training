# -*- coding: utf-8 -*
import pytest
from group import Group
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    return fixture


def test_add_group(app):
    app.login(user_name="admin", password="secret")
    app.open_groups_page()
    app.create_group(Group(name="test", header="1234", footer="@#$%"))
    app.logout()
    # time.sleep(10)


def test_add_empty_group(app):
    app.login(user_name="admin", password="secret")
    app.open_groups_page()
    app.create_group(Group(name="", header="", footer=""))
    app.logout()
