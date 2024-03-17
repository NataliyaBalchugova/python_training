from model.contact import Contact


# def test_add_contact(app):
#     old_contacts = app.contact.get_contact_list()
#     app.contact.fill_contact(Contact(firstname="Alexandr", lastname="Ponomarev", work="System Administrator", address="Demakova, 5"))
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) + 1 == len(new_contacts)

def test_add_contact(app):

    old_contacts = app.contact.get_contact_list()
    app.contact.fill_contact(Contact(firstname="Alexandr", lastname="Ponomarev", workphone="234234",
                                     address="Demakova, 5", homephone= "homephone12", mobilephone="mobilephone0",
                                     secondaryphone="secondaryphone23"))
    assert len(old_contacts) + 1 == app.contact.count_contacts()
    new_contacts = app.contact.get_contact_list()


