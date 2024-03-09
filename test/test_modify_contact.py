from model.contact import Contact


def test_modify_contact_name(app):
    if app.contact.el_exist():
        pass
    else:
        app.contact.create_contact(Contact(firstname="Alexandr", lastname="Ponomarev", work="System Administrator",
                                           address="Demakova, 5"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_firstname_contact(Contact(firstname="New firstname2355", lastname="New 1", work="11"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)