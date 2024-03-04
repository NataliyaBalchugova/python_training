from model.contact import Contact


def test_del_first_contact(app):
    # if app.contact.count_contacts() == '0':
    if app.contact.el_exist():
        pass
    else:
        app.contact.create_contact(Contact(firstname="Alexandr", lastname="Ponomarev", work="System Administrator",
                                           address="Demakova, 5"))
    app.contact.delete_first_contact()

