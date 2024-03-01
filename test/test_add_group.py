# -*- coding: utf-8 -*
from model.group import Group


def test_add_group(app):
    app.group.open_groups_page()
    old_groups = app.group.get_group_list()
    group = Group(name="test", header="1234", footer="@#$%")
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    # time.sleep(10)

# def test_add_empty_group(app):
    # app.group.open_groups_page()
#    old_groups = app.group.get_groups_list()
#    group = Group(name="", header="", footer="")
#    app.group.create(group)
#    new_groups = app.group.get_groups_list()
#    assert len(old_groups) + 1 == len(new_groups)
#    old_groups.append(group)
#    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
