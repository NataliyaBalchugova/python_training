from model.contact import Contact
from random import randrange


def test_del_some_contact(app):
    if app.contact.el_exist():
        #print('\nel_exist pass')
        pass
    else:
        #print('\n0 contacts on page, create new one')
        app.contact.create_contact(Contact(firstname="Alexandr", lastname="Ponomarev", work="System Administrator",
                                           address="Demakova, 5"))
    old_contacts = app.contact.get_contact_list()
    # random index
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    #old_contacts[index:index+1] = []
   # assert old_contacts == new_contacts
