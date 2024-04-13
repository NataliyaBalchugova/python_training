# -*- coding: utf-8 -*
from generator.group import generate
from model.group import Group
json_groups = generate()

def test_add_group(app, db, json_groups):
    group = json_groups
    app.group.open_groups_page()
    old_groups = db.get_group_list()
    app.group.create(group)
    new_groups = db.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


