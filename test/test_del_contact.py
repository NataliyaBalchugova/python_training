from model.contact import Contact
from random import randrange
import random


def test_del_some_contact(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create_contact(Contact(firstname="Alexandr", lastname="Ponomarev", work="S1212",
                                           address="Demakova, 5"))
    old_contacts = db.get_contact_list()
    # random index
    # index = randrange(len(old_contacts))
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    #old_contacts[index:index+1] = []
    #assert old_contacts == new_contacts
