from model.contact import Contact
from random import randrange


def test_modify_contact_name(app):
    if app.contact.el_exist():
        pass
    else:
        app.contact.create_contact(Contact(firstname="Alexandr", lastname="Ponomarev", address="Demakova, 5",
                                           homephone="homephone12", mobilephone="mobilephone0",
                                           workphone="wne34", secondaryphone="sece23"))
    contact = Contact(firstname="asd", lastname="qwe", address="Demakova, 6", homephone="homephone12",
                      mobilephone="mobine0", workphone="wore34", secondaryphone="seconne23",
                      first_email="345sd", second_email="345werwe", third_email="347werwer")
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.modify_contact_by_index(contact, index)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)