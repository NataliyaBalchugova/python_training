# -*- coding: utf-8 -*
import pytest
from model.group import Group
from fixture.application import Application

def test_add_group(app):
    # app.group.open_groups_page()
    old_groups = app.group.get_groups_list()
    app.group.create(Group(name="test", header="1234", footer="@#$%"))
    new_groups = app.group.get_groups_list()
    assert len(old_groups) + 1 == len(new_groups)
    # time.sleep(10)


def test_add_empty_group(app):
    # app.group.open_groups_page()
    old_groups = app.group.get_groups_list()
    app.group.create(Group(name="", header="", footer=""))
    new_groups = app.group.get_groups_list()
    assert len(old_groups) + 1 == len(new_groups)

