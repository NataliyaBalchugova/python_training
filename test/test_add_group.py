# -*- coding: utf-8 -*
import pytest
from model.group import Group
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    return fixture


def test_add_group(app):
    app.session.login(user_name="admin", password="secret")
    app.group.open_groups_page()
    app.group.create(Group(name="test", header="1234", footer="@#$%"))
    app.session.logout()
    # time.sleep(10)


def test_add_empty_group(app):
    app.session.login(user_name="admin", password="secret")
    app.group.open_groups_page()
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()