from model.contact import Contact


def test_modify_contact_name(app, db):
    if app.contact.el_exist():
        pass
    else:
        app.contact.create_contact(Contact(firstname="Alex", lastname="Ivanov", address="Demakova, 95",
                                           homephone="homephone12", mobilephone="mobilephone0",
                                           workphone="wne34", secondaryphone="sece23"))
    contact = Contact(firstname="asd", lastname="qwe", address="Demakova, 6", homephone="homephone12",
                      mobilephone="mobine0", workphone="wore34", secondaryphone="seconne23",
                      first_email="345sd", second_email="345werwe", third_email="347werwer")
    old_contacts = db.get_contact_list()
    app.contact.modify_contact_by_id(contact, id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)