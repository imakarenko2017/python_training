
from model.contact import Contact


def test_modify_first_contact(app):
    if app.contact.count()==0:
       app.contact.create(Contact(firstname="Inna",middlename="I",lastname="Makarenko",birthday="3",birthmonth="March",birthyear="1980",email="inna.makarenko@gmail.com"))
    contact=Contact(lastname="Makarenko",firstname="Inna")
    old_contacts = app.contact.get_contacts_list()
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    app.contact.open_contacts_page()
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=contact.id_or_max) == sorted(new_contacts, key=contact.id_or_max)