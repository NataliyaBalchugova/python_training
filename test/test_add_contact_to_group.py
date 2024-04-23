from fixture.orm import ORMFixture
from model.group import Group

def test_add_contact_to_group(app):
    db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
    old_contacts_in_group = db.get_contacts_in_group(Group(id="463"))
    app.contact.add_contact_in_group(Group(id="463"))
    new_contacts_in_group = db.get_contacts_in_group(Group(id="463"))
    assert len(old_contacts_in_group) + 1 == len(new_contacts_in_group)


