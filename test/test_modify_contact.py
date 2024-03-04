from model.contact import Contact


def test_modify_contact_name(app):
    app.contact.modify_firstname_contact(Contact(firstname="New firstname2355", lastname="New 1", work= "11"))