from model.group import Group


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test", header="1", footer="2"))
    app.group.modify_first_group(Group(name="New group", header="1234", footer="@#$%"))

# def test_modify_group_header(app):
#     app.session.login(user_name="admin", password="secret")
#     app.group.modify_first_group(Group(header="New header"))
#     app.session.logout()