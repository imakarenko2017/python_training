
from model.contact import Contact
from random import randrange

def test_delete_some_contact (app):
    if app.contact.count() ==0:
        app.contact.create(Contact(firstname="Inessa",lastname="Molchanova"))
    old_contacts = app.contact.get_contacts_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    app.contact.open_contacts_page()
    new_contacts = app.contact.get_contacts_list()
    assert len(new_contacts) == len(old_contacts) - 1

def test_delete_first_contact (app):
    if app.contact.count() ==0:
        app.contact.create(Contact(firstname="Inessa",lastname="Molchanova"))
    old_contacts = app.contact.get_contacts_list()
    app.contact.delete_first_contact()
    app.contact.open_contacts_page()
    new_contacts = app.contact.get_contacts_list()
    assert len(new_contacts) == len(old_contacts) - 1


