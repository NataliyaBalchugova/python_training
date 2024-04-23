from generator.contact import generate
json_contacts = generate()


def test_add_contact(app, db, json_contacts):
    contact = json_contacts
    app.contact.open_contact_page()
    old_contacts = db.get_contact_list()
    app.contact.fill_contact(contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)