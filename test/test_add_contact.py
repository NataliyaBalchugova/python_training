from model.contact import Contact


def test_add_contact(app):
    app.contact.fill_contact(Contact(firstname="Alexandr", lastname="Ponomarev", work="System Administrator",
                                      address="Demakova, 5"))
