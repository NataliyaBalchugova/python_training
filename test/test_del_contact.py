from model.contact import Contact


def test_del_first_contact(app):
    if app.contact.el_exist():
        print('\nel_exist pass')
        pass
    else:
        print('\n0 contacts on page, create new one')
        app.contact.create_contact(Contact(firstname="Alexandr", lastname="Ponomarev", work="System Administrator",
                                           address="Demakova, 5"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
