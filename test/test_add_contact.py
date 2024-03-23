from model.contact import Contact
import random
import string
import pytest
import time
def random_string_contact(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata_contact = [Contact(
                                                        firstname=random_string_contact("firstname", 10),
                                                        lastname=random_string_contact("lastname", 20),
                                                        address=random_string_contact("address", 20),
                                                        workphone=random_string_contact("address", 30),
                                                        homephone=random_string_contact("home", 8),
                                                        mobilephone=random_string_contact("mobile", 8),
                                                        secondaryphone=random_string_contact("secondaryphone", 8),
                                                        first_email=random_string_contact("email", 10),
                                                        second_email=random_string_contact("email2", 40),
                                                        third_email=random_string_contact("email3", 40))

    for i in range(5)
                                                    ]


# def test_add_contact(app):
#     old_contacts = app.contact.get_contact_list()
#     app.contact.fill_contact(Contact(firstname="Alexandr", lastname="Ponomarev", work="System Administrator", address="Demakova, 5"))
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) + 1 == len(new_contacts)

@pytest.mark.parametrize("contact", testdata_contact, ids=[repr(x) for x in testdata_contact])
def test_add_contact(app, contact):
    app.contact.open_contact_page()
    #time.sleep(4)
    old_contacts = app.contact.get_contact_list()
    app.contact.fill_contact(contact)
    assert len(old_contacts) + 1 == app.contact.count_contacts()
    #new_contacts = app.contact.get_contact_list()


