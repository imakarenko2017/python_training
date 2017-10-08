
from model.contact import Contact
from random import randrange

def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Alexey",middlename="I",lastname="Pavlov",birthday="3",birthmonth="March",birthyear="1980",email="inna.makarenko@gmail.com"))
    old_contacts = app.contact.get_contacts_list()
    index = randrange(len(old_contacts))
    contact=Contact(firstname="New FN",lastname="New LN",email="inna@gmail.com")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index,contact)
    app.contact.open_contacts_page()
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)