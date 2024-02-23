# -*- coding: utf-8 -*
import pytest
from model.group import Group
from fixture.application import Application


# @pytest.fixture
# def app(request):
#     fixture = Application()
#     return fixture


def test_add_group(app):
    app.group.open_groups_page()
    app.group.create(Group(name="test", header="1234", footer="@#$%"))
    # time.sleep(10)


def test_add_empty_group(app):
    app.group.open_groups_page()
    app.group.create(Group(name="", header="", footer=""))
