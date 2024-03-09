from model.contact import Contact


def test_del_first_contact(app):
    # if app.contact.count_contacts() == '0':
    if app.contact.el_exist():
        pass
    else:
        app.contact.create_contact(Contact(firstname="Alexandr", lastname="Ponomarev", work="System Administrator",
                                           address="Demakova, 5"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)

