
from model.contact import Contact


def test_delete_first_contact (app):
    if app.contact.count() ==0:
        app.contact.create(Contact(firstname="Inessa",lastname="Molchanova"))
    old_contacts = app.contact.get_contacts_list()
    app.contact.delete_first_contact()
    app.contact.open_contacts_page()
    new_contacts = app.contact.get_contacts_list()
    assert len(new_contacts) == len(old_contacts) - 1


