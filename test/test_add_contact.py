
def test_add_contact(app, json_contacts):
    contact = json_contacts
    app.contact.open_contact_page()
    #time.sleep(4)
    old_contacts = app.contact.get_contact_list()
    app.contact.fill_contact(contact)
    assert len(old_contacts) + 1 == app.contact.count_contacts()
    #new_contacts = app.contact.get_contact_list()


