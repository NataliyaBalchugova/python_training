from fixture.orm import ORMFixture
from model.group import Group
from model.contact import Contact
from random import randrange
import random




def test_add_contact_to_group(app, group):
    db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
    old_contacts_in_group=db.get_contacts_in_group(group)
    group = random.choice(old_contacts_in_group)
    old_contacts_in_group = db.get_contacts_in_group(group.group_id)
    app.contact.add_contact_in_group(group.group_id)
    new_contacts_in_group = db.get_contacts_not_in_group(group.group_id)
    assert len(old_contacts_in_group) + 1 == len(new_contacts_in_group)


