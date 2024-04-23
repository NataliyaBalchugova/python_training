from model.contact import Contact
import random


def test_del_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create_contact(Contact(firstname="Alexandr", lastname="Ponomarev", workphone="S1212", homephone="",
                                           mobilephone="89231566457", secondaryphone="---", first_email="bn@yandex.ru", second_email="=-",
                                           third_email="-", address="Demakova, 5"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)