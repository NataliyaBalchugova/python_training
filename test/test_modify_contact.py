from model.contact import Contact
from random import randrange


def test_modify_contact_name(app):
    if app.contact.el_exist():
        pass
    else:
        app.contact.create_contact(Contact(firstname="Alexandr", lastname="Ponomarev", work="System Administrator",
                                           address="Demakova, 5"))
    contact = Contact(firstname="asd", lastname="qwe", work="11")
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.modify_contact_by_index(contact, index)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)